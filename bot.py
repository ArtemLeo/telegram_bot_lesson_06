import asyncio
import logging
import sys
from typing import List, Dict, Any, Optional, Tuple

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, URLInputFile, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config import BOT_TOKEN as TOKEN
from commands import FILMS_COMMAND, START_COMMAND, FILM_CREATE_COMMAND, BOT_COMMANDS
from data import get_films, add_film, save_films
from keyboards import films_keyboard_markup, FilmCallback
from models import Film
from logger import async_log_function

dp = Dispatcher()


class FilmForm(StatesGroup):
    """A class that defines states for obtaining information about a film."""
    name = State()
    description = State()
    rating = State()
    genre = State()
    actors = State()
    poster = State()


class FilmStates(StatesGroup):
    """A class that defines states for various film operations."""
    search_query = State()
    filter_criteria = State()
    delete_query = State()
    edit_query = State()
    edit_description = State()
    rate_query = State()
    set_rating = State()


@dp.message(Command("start"))
@async_log_function
async def start(message: Message) -> None:
    """
    Handler for the /start command.
    The function sends a welcome message to the user.

    Arguments:
        message (Message): Message from the user.
    """
    try:
        await message.answer(
            f"Hello🖐, {html.bold(message.from_user.full_name)}!\n"
            "I'm your first Telegram Bot 🥳"
        )
    except Exception as e:
        logging.error(f"Error in start command: {e}")


@dp.message(FILMS_COMMAND)
@async_log_function
async def films(message: Message) -> None:
    """
    Handler for the /films command.
    The function sends a list of films to the user.

    Arguments:
        message (Message): Message from the user.
    """
    try:
        data = get_films()
        markup = films_keyboard_markup(films_list=data)
        await message.answer(
            f"<b>Список фільмів: 🎬</b>\nОберіть фільм, щоб отримати інформацію про нього.",
            reply_markup=markup
        )
    except Exception as e:
        logging.error(f"Error in films command: {e}")
        await message.answer("Виникла помилка при отриманні списку фільмів.")


@dp.callback_query(FilmCallback.filter())
@async_log_function
async def callback_film(callback: CallbackQuery, callback_data: FilmCallback) -> None:
    """
    Callback handler for films.
    The function sends detailed information about the selected film.

    Arguments:
        callback (CallbackQuery): Callback from the user.
        callback_data (FilmCallback): Callback data.
    """
    try:
        film_id: int = callback_data.id
        film_data: Dict[str, Any] = get_films(film_id=film_id)
        film: Film = Film(**film_data)
        text: str = (
            f"<b>Фільм:</b> {film.name}\n"
            f"<b>Опис:</b> {film.description}\n"
            f"<b>Рейтинг:</b> {film.rating}\n"
            f"<b>Жанр:</b> {film.genre}\n"
            f"<b>Актори:</b> {', '.join(film.actors)}\n"
        )
        await callback.message.answer_photo(
            caption=text,
            photo=URLInputFile(
                film.poster,
                filename=f"{film.name}_poster.{film.poster.split('.')[-1]}"
            )
        )
    except Exception as e:
        logging.error(f"Error in callback_film: {e}")
        await callback.message.answer("Виникла помилка при отриманні інформації про фільм.")


@dp.message(FILM_CREATE_COMMAND)
@async_log_function
async def film_create(message: Message, state: FSMContext) -> None:
    """
    Start the process of creating a new film.
    The function asks the user for the film's name.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    try:
        await state.set_state(FilmForm.name)
        await message.answer(
            f"<b>Введіть назву фільму ...</b>",
            reply_markup=ReplyKeyboardRemove(),
        )
    except Exception as e:
        logging.error(f"Error in film_create: {e}")
        await message.answer("Виникла помилка при створенні фільму.")


@dp.message(FilmForm.name)
@async_log_function
async def film_name(message: Message, state: FSMContext) -> None:
    """
    The function receives the film name and asks for the film description.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    try:
        await state.update_data(name=message.text)
        await state.set_state(FilmForm.description)
        await message.answer(
            f"<b>Введіть опис фільму ...</b>",
            reply_markup=ReplyKeyboardRemove(),
        )
    except Exception as e:
        logging.error(f"Error in film_name: {e}")
        await message.answer("Виникла помилка при введенні назви фільму.")


@dp.message(FilmForm.description)
@async_log_function
async def film_description(message: Message, state: FSMContext) -> None:
    """
    The function receives the film description and asks for the film rating.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    try:
        await state.update_data(description=message.text)
        await state.set_state(FilmForm.rating)
        await message.answer(
            f"<b>Вкажіть рейтинг фільму (від 0 до 10) ...</b>",
            reply_markup=ReplyKeyboardRemove(),
        )
    except Exception as e:
        logging.error(f"Error in film_description: {e}")
        await message.answer("Виникла помилка при введенні опису фільму.")


@dp.message(FilmForm.rating)
@async_log_function
async def film_rating(message: Message, state: FSMContext) -> None:
    """
    The function receives the film rating and asks for the film genre.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    try:
        await state.update_data(rating=float(message.text))
        await state.set_state(FilmForm.genre)
        await message.answer(
            f"<b>Введіть жанр фільму ...</b>",
            reply_markup=ReplyKeyboardRemove(),
        )
    except ValueError:
        await message.answer("Рейтинг повинен бути числом від 0 до 10.")
    except Exception as e:
        logging.error(f"Error in film_rating: {e}")
        await message.answer("Виникла помилка при введенні рейтингу фільму.")


@dp.message(FilmForm.genre)
@async_log_function
async def film_genre(message: Message, state: FSMContext) -> None:
    """
    The function receives the film genre and asks for the film actors.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    try:
        await state.update_data(genre=message.text)
        await state.set_state(FilmForm.actors)
        await message.answer(
            text=f"<b>Введіть акторів фільму через `, ` \n⚠️ (Обов'язкова кома та відступ після неї)</b>",
            reply_markup=ReplyKeyboardRemove(),
        )
    except Exception as e:
        logging.error(f"Error in film_genre: {e}")
        await message.answer("Виникла помилка при введенні жанру фільму.")


@dp.message(FilmForm.actors)
@async_log_function
async def film_actors(message: Message, state: FSMContext) -> None:
    """
    The function receives the film actors and asks for the film poster link.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    try:
        await state.update_data(actors=[x for x in message.text.split(", ")])
        await state.set_state(FilmForm.poster)
        await message.answer(
            f"<b>Введіть посилання на постер фільму ...</b>",
            reply_markup=ReplyKeyboardRemove(),
        )
    except Exception as e:
        logging.error(f"Error in film_actors: {e}")
        await message.answer("Виникла помилка при введенні акторів фільму.")


@dp.message(FilmForm.poster)
@async_log_function
async def film_poster(message: Message, state: FSMContext) -> None:
    """
    The function receives the film poster link and completes the film creation process.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    try:
        data: Dict[str, Any] = await state.update_data(poster=message.text)
        film: Film = Film(**data)
        add_film(film.model_dump())
        await state.clear()
        await message.answer(
            f"<b>Фільм {film.name} успішно додано ✅</b>",
            reply_markup=ReplyKeyboardRemove(),
        )
    except Exception as e:
        logging.error(f"Error in film_poster: {e}")
        await message.answer("Виникла помилка при додаванні фільму.")


@dp.message(Command("search_film"))
async def search_film(message: Message, state: FSMContext) -> None:
    """
    Start the process of searching for a film by name.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    await state.set_state(FilmStates.search_query)
    await message.reply("<b>Введіть назву фільму для пошуку:</b>")


@dp.message(FilmStates.search_query)
@async_log_function
async def get_search_query(message: Message, state: FSMContext) -> None:
    """
    The function receives the film name for search and sends the search results.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    query: str = message.text.lower()
    films_data: List[Dict[str, Any]] = get_films()
    results: List[Dict[str, Any]] = [film for film in films_data if query in film['name'].lower()]

    if results:
        for film_data in results:
            film: Film = Film(**film_data)
            text: str = (
                f"<b>Фільм:</b> {film.name}\n"
                f"<b>Опис:</b> {film.description}\n"
                f"<b>Рейтинг:</b> {film.rating}\n"
                f"<b>Жанр:</b> {film.genre}\n"
                f"<b>Актори:</b> {', '.join(film.actors)}\n"
            )
            await message.answer_photo(
                caption=text,
                photo=URLInputFile(
                    film.poster,
                    filename=f"{film.name}_poster.{film.poster.split('.')[-1]}"
                )
            )
    else:
        await message.reply("<b>Фільм не знайдено!</b>")
    await state.clear()


@dp.message(Command("filter_films"))
@async_log_function
async def filter_film(message: Message, state: FSMContext) -> None:
    """
    Start the process of filtering films by genre.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    await state.set_state(FilmStates.filter_criteria)
    await message.reply("<b>Введіть жанр фільму для фільтрації:</b>")


@dp.message(FilmStates.filter_criteria)
@async_log_function
async def get_filter_criteria(message: Message, state: FSMContext) -> None:
    """
    The function receives the film genre for filtering and sends the filtered results.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    criteria: str = message.text.lower()
    films_data: List[Dict[str, Any]] = get_films()
    filtered: List[Dict[str, Any]] = list(filter(
        lambda film: criteria in film['genre'].lower(),
        films_data
    ))

    if filtered:
        for film_data in filtered:
            film: Film = Film(**film_data)
            text: str = (
                f"<b>Фільм:</b> {film.name}\n"
                f"<b>Опис:</b> {film.description}\n"
                f"<b>Рейтинг:</b> {film.rating}\n"
                f"<b>Жанр:</b> {film.genre}\n"
                f"<b>Актори:</b> {', '.join(film.actors)}\n"
            )
            await message.answer_photo(
                caption=text,
                photo=URLInputFile(
                    film.poster,
                    filename=f"{film.name}_poster.{film.poster.split('.')[-1]}"
                )
            )
    else:
        await message.reply("<b>Фільмів за вказаним жанром не знайдено.</b>")
    await state.clear()


@dp.message(Command("delete_film"))
@async_log_function
async def delete_film(message: Message, state: FSMContext) -> None:
    """
    Start the process of deleting a film by name.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    await message.reply("<b>Введіть назву фільму, який бажаєте видалити:</b>")
    await state.set_state(FilmStates.delete_query)


@dp.message(FilmStates.delete_query)
@async_log_function
async def get_delete_query(message: Message, state: FSMContext) -> None:
    """
    The function receives the film name for deletion and deletes the film.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    film_to_delete: str = message.text.lower()
    films_data: List[Dict[str, Any]] = get_films()

    for film in films_data:
        if film_to_delete == film['name'].lower():
            films_data.remove(film)
            save_films(films_data)
            await message.reply(f"<b>Фільм '{film['name']}' видалено ✅</b>")
            await state.clear()
            return

    await message.reply("<b>Фільм не знайдено!</b>")
    await state.clear()


@dp.message(Command("edit_film"))
@async_log_function
async def edit_film(message: Message, state: FSMContext) -> None:
    """
    Start the process of editing film information.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    films_data: List[Dict[str, Any]] = get_films()
    if not films_data:
        await message.reply("<b>Список фільмів порожній. Немає що редагувати.</b>")
        return

    film_names: str = "\n".join([f"- {film['name']}" for film in films_data])
    await message.reply(
        "<b>Введіть назву фільму, який бажаєте редагувати:</b>\n"
        f"Доступні фільми:\n{film_names}"
    )
    await state.set_state(FilmStates.edit_query)


@dp.message(FilmStates.edit_query)
@async_log_function
async def get_edit_query(message: Message, state: FSMContext) -> None:
    """
    The function receives the film name for editing and asks for the field to edit.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    film_name: str = message.text.strip()
    films_data: List[Dict[str, Any]] = get_films()
    film_found: Optional[Dict[str, Any]] = None

    for film in films_data:
        if film_name.lower() == film['name'].lower():
            film_found = film
            break

    if not film_found:
        await message.reply("<b>Фільм не знайдено!</b>")
        await state.clear()
        return

    await state.update_data(film=film_found, films_data=films_data)
    await message.reply(
        "<b>Введіть поле для редагування та нове значення у форматі:</b>\n"
        "<code>поле|нове значення</code>\n\n"
        "<b>Доступні поля:</b> name, description, rating, genre, actors, poster\n"
        "<b>Приклад:</b> <code>rating|9.5</code>"
    )
    await state.set_state(FilmStates.edit_description)


@dp.message(FilmStates.edit_description)
@async_log_function
async def process_edit(message: Message, state: FSMContext) -> None:
    """
    The function receives the field and new value for editing the film and updates the information.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    try:
        data: Dict[str, Any] = await state.get_data()
        film: Dict[str, Any] = data['film']
        films_data: List[Dict[str, Any]] = data['films_data']

        if '|' not in message.text:
            raise ValueError("Невірний формат. Використовуйте '|' для розділення поля та значення")

        field: str
        new_value: Any
        field, new_value = message.text.split('|', 1)
        field = field.strip().lower()
        new_value = new_value.strip()

        valid_fields: List[str] = ['name', 'description', 'rating', 'genre', 'actors', 'poster']
        if field not in valid_fields:
            raise ValueError(f"Невірне поле. Доступні: {', '.join(valid_fields)}")

        if field == 'rating':
            try:
                new_value = float(new_value)
                if not 0 <= new_value <= 10:
                    raise ValueError("Рейтинг повинен бути від 0 до 10")
            except ValueError:
                raise ValueError("Рейтинг повинен бути числом (наприклад, 8.5)")
        elif field == 'actors':
            new_value = [actor.strip() for actor in new_value.split(',')]

        for f in films_data:
            if f['name'] == film['name']:
                f[field] = new_value
                break

        save_films(films_data)
        await message.reply(
            f"<b>Фільм '{film['name']}' успішно оновлено!</b>\n"
            f"<b>{field}:</b> {new_value}"
        )
        await state.clear()
    except Exception as e:
        await message.reply(
            f"<b>Помилка:</b> {str(e)}\n"
            "<b>Використовуйте формат:</b>\n"
            "<code>поле|нове значення</code>\n"
            "<b>Приклад:</b> <code>rating|9.5</code>"
        )
        await state.clear()


@dp.message(Command("recommend_film"))
@async_log_function
async def recommend_film(message: Message) -> None:
    """
    The function recommends films with the highest ratings.

    Arguments:
        message (Message): Message from the user.
    """
    films_data: List[Dict[str, Any]] = get_films()
    rated_films: List[Dict[str, Any]] = [film for film in films_data if film.get('rating') is not None]

    if not rated_films:
        await message.reply("<b>На жаль, немає фільмів з рейтингом для рекомендації.</b>")
        return

    top_films: List[Dict[str, Any]] = sorted(rated_films, key=lambda x: float(x['rating']), reverse=True)[:3]
    await message.reply("<b>🍿 Best ⭐️ Films:</b>")

    for i, film_data in enumerate(top_films, 1):
        film: Film = Film(**film_data)
        text: str = (
            f"<b>#{i} Рекомендований фільм:</b>\n"
            f"<b>Назва:</b> {film.name}\n"
            f"<b>Опис:</b> {film.description}\n"
            f"<b>Рейтинг:</b> ⭐️ {film.rating}/10\n"
            f"<b>Жанр:</b> {film.genre}\n"
            f"<b>Актори:</b> {', '.join(film.actors)}\n"
        )
        await message.answer_photo(
            caption=text,
            photo=URLInputFile(
                film.poster,
                filename=f"{film.name}_poster.{film.poster.split('.')[-1]}"
            ),
            parse_mode="HTML"
        )


async def main() -> None:
    """
    Main asynchronous function to run the bot.
    Initializes the bot and starts the polling loop to receive updates.
    """
    try:
        bot: Bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        await bot.set_my_commands(BOT_COMMANDS)
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Error in main: {e}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())