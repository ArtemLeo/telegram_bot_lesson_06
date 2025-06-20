# ✅ Урок 46: Оформлення коду та документація

---
<img src="main_image.png" alt="pygame" width="1500">

## Зміст уроку:

1. [Сьогодні на уроці](#1-сьогодні-на-уроці)
2. [Стиль коду. `PEP 8`. Рефакторинг коду](#2-стиль-коду-pep-8-рефакторинг-коду)
3. [Documentation String (`Docstring`)](#3-docstring-documentation-string)
4. [**Анотації типів** `Annotation types`](#4-анотації-типів-annotation-types)
5. [Реалізація `Docstring`](#5-реалізація-docstring)
6. [Реалізація `Annotation types`](#6-реалізація-annotation-types)
7. [Реалізація `Exception Handling`](#7-реалізація-exception-handling)
8. [Реалізація `Testing`](#8-реалізація-testing)
9. [Підведення підсумків 🚀](#9-підведення-підсумків-)
10. [Домашнє завдання 🏠](#10-домашнє-завдання-)

> 🔗 Useful Links:

- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)

---

## 1. Сьогодні на уроці

> 💡 На цьому уроці ми розглянемо наступні теми:

- Стиль коду. `PEP 8`. Рефакторинг коду
- Documentation String (`Docstring`)
- Анотації типів (`Annotation types`)
- Реалізація `Docstring`
- Реалізація `Annotation types`
- Реалізація `Exception Handling`
- Реалізація `Testing`

[Повернутися до змісту](#зміст-уроку)

---

## 2. Стиль коду. PEP 8. Рефакторинг коду

> 💡 **Стиль кодування** (**Code Style**) - це набір правил та рекомендацій для написання зрозумілого коду, що є ключем
> до успішної **співпраці** в команді розробників.

> 💡 **PEP8** - це документ, що містить **рекомендації** (домовленості) стосовно стилю
> кодування на мові Python.

- Незалежно від того, скільки людей працює над проєктом, весь код повинен виглядати так, ніби його написала одна
  людина.
- Такий підхід спрощує розуміння коду і сприяє більш ефективній командній роботі.
- PEP 8 містить рекомендації щодо **відступів**, **довжини рядка**, **порожніх рядків**, **імпортів**, та багато інших
  аспектів кодування, що дозволяє будь-якому розробнику швидко і легко **зрозуміти** бізнес-логіку, реалізовану іншим
  розробником.
- Стиль коду дуже важливий не для компілятора чи інтерпретатора а для людини, яка буде розбиратись у цьому коді.
- Python **дозволяє** написати код **без відступів**, використання **функцій**, практик **ООП** та інших переваг мови, і
  код буде **працювати**.
- Однак через `2-3` дні навіть автор може не зрозуміти власний код, що призводить до появи такої **негативної
  характеристики**, як **низький рівень читабельності коду**.

### Основні рекомендації **PEP 8**:

> **Відступи та Пробіли**:

- Використовуйте `4` пробіли для кожного **рівня вкладеності** (нового блоку коду).
- Відступи в Python використовуються для визначення блоків коду, які є ключовим аспектом синтаксису мови.
- Додавання пробілів навколо операторів (`+`, `-`, `*` тощо) робить код набагато легшим для читання і допомагає швидше
  зрозуміти логіку виразів.

> **Максимальна довжина рядка**:

Обмежуйте довжину рядків програми до `79` символів.

> **Лапки в рядках**:

Використовуйте **одинарні** або **подвійні** лапки, але необхідно дотримуватися одного стилю.

> **Кодування вихідного файлу**:

Використовуйте `UTF-8`

> **Імпорти**:

- Імпорти завжди розміщуються у верхній частині файлу.
- Необхідно групувати імпорти в наступному порядку: **стандартні** бібліотеки, **сторонні** бібліотеки, **локальні**
  модулі.
- Кожен імпорт нового модуля повинен знаходитись на **окремому рядку**.

**⚠️ Bad Practice**:

```python
import sys, os
```

**✅ Good Practice**:

```python
import os
import sys
```

**⚠️ Bad Practice**:

```text
def sum(x, y):
 return x + y  # 1 space
```

**✅ Good Practice**:

```text
def sum(x, y):
    return x + y  # 4 spaces
```

**⚠️ Bad Practice**:

```text
def area(width,length):
    return width*length
```

**✅ Good Practice**:

```text
def area(width, length):
    return width * length
```

> 💡 **Рефакторинг** (`Refactoring`) - це покращення існуючого коду без зміни його поведінки.

- Рефакторинг упорядковує код для підвищення його читабельності та підтримки, зберігаючи його функціональність.
- Наприклад, заміна повторюваних ділянок коду на виклик однієї функції або розбиття довгої функції на кілька менших.

### 🧩 For Example:

Програма обчислює середню оцінку студента.

```python
# Before refactoring
def calculate_average(grades):
    total = 0
    count = 0
    for grade in grades:
        total += grade
        count += 1
    average = total / count
    return average
```

Код працює, але його можна зробити більш читабельним та лаконічним.

Використаємо вбудовані функції `sum()` та `len()`, щоб спростити обчислення середнього значення.

```python
# After refactoring
def calculate_average(grades: list) -> float:
    return sum(grades) / len(grades)
```

### 🧩 Завдання 1:

Проведіть аналіз наступних варіантів однакового коду:

- Який з варіантів більш зрозумілий?
- Що відбувається в цьому скрипті?

**⚠️ Bad Practice**:

```text
from sqlalchemy import create_engine
from sqlalchemy.orm import (
   MappedAsDataclass,
   DeclarativeBase,
   scoped_session,
   sessionmaker,
)
class Base(MappedAsDataclass, DeclarativeBase):
   pass
from .models import Tour, Direction
engine = create_engine("sqlite:///my_db.db", echo=True)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
from .crud import CRUD
def migrate():
   session = Session()
   japan_direction = Direction("Японія", "підтекст", "опис")
   japan_tour = Tour(
       "Квітучі сакури",
       4,
       18,
       "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Emperor_Jimmu.jpg/800px-Emperor_Jimmu.jpg",
       "Опис туру",
       "Японія",
       japan_direction,
   )
   japan_tour2 = Tour(
       "Квітучі сакури",
       4,
       18,
       "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Emperor_Jimmu.jpg/800px-Emperor_Jimmu.jpg",
       "Опис туру",
       "Японія",
       japan_direction,
   )
   session.add(japan_direction)
   session.commit()
migrate()
```

**✅ Good Practice**:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    MappedAsDataclass,
    DeclarativeBase,
    scoped_session,
    sessionmaker,
)


class Base(MappedAsDataclass, DeclarativeBase):
    pass


from .models import Tour, Direction

engine = create_engine("sqlite:///my_db.db", echo=True)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

from .crud import CRUD


def migrate():
    session = Session()
    japan_direction = Direction("Японія", "підтекст", "опис")
    japan_tour = Tour(
        "Квітучі сакури",
        4,
        18,
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Emperor_Jimmu.jpg/800px-Emperor_Jimmu.jpg",
        "Опис туру",
        "Японія",
        japan_direction,
    )
    japan_tour2 = Tour(
        "Квітучі сакури",
        4,
        18,
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Emperor_Jimmu.jpg/800px-Emperor_Jimmu.jpg",
        "Опис туру",
        "Японія",
        japan_direction,
    )
    session.add(japan_direction)
    session.commit()


migrate()
```

Другий варіант більш зрозумілий, тому що він має краще форматування з відступами та порожніми рядками, які покращують
читабельність.

У скрипті створюється база даних, додаються нові записи та виконується міграція даних.

### 🧩 Завдання 2:

Проведіть аналіз наступних варіантів однакового коду:

- Який з варіантів більш зрозумілий?
- Що відбувається в цьому скрипті?

**⚠️ Bad Practice**:

```text
import json
opened_file = open(
   file="data.json",
   mode="r",
   encoding="utf-8",
)
data = json.load(fp=opened_file)
opened_file.close()
for person in data:
   print(f"{person.get('id')} -> {person.get('name')}")
data.sort(key=lambda x: x.get("id"))
for person in data:
   print(f"{person.get('id')} -> {person.get('name')}")
person.update({"name": "Ezio Auditore da Firenze"})
opened_file = open(
   file="data.json",
   mode="w",
   encoding="utf-8",
)
json.dump(
   obj=data,
   fp=opened_file,
   indent=4,
)
```

**✅ Good Practice**:

```python
import json


def read_json_data(file_path: str = "data.json") -> list[dict]:
    with open(
            file=file_path,
            mode="r",
            encoding="utf-8",
    ) as opened_file:
        data = json.load(fp=opened_file)
    return data


def show_data(data: list[dict]) -> None:
    """
    Prints all data items in formatted row
    """
    for person in data:
        print(f"{person.get('id')} -> {person.get('name')}")


def write_json_data(
        data: list[dict],
        file_path: str = "data.json",
) -> None:
    with open(
            file=file_path,
            mode="w",
            encoding="utf-8",
    ) as opened_file:
        json.dump(
            obj=data,
            fp=opened_file,
            indent=4,
        )


def main():
    data = read_json_data(file_path="data.json")

    show_data(data)

    data.sort(key=lambda x: x.get("id"))

    show_data(data)

    data[-1].update({"name": "Ezio Auditore da Firenze"})

    write_json_data(file_path="data.json", data=data)


if __name__ == "__main__":
    main()
```

Другий варіант більш зрозумілий, тому що він використовує функції для структурування коду та покращення читабельності.

Скрипт зчитує дані з JSON файлу, виводить їх, сортує, оновлює ім'я останнього елементу та записує дані назад у файл.

[Повернутися до змісту](#зміст-уроку)

---

## 3. Docstring (`Documentation String`)

> 💡 **Docstring** - це рядок документації (коментар), який використовується для пояснення структури та роботи
> **модуля**, **класу**, **метода** або **функції**.

- **Docstring** також може містити детальну інформацію про **параметри** блоку коду, або **приклади-тести** його
  використання.
- Синтаксично **Docstring** починається та закінчується **потрійними лапками** (`"""` або `'''`)

### 🧩 For Example:

```python
def sum_numbers(num1: float, num2: float) -> float:
    """
    Calculate the sum of two numbers.

    Parameters:
    - num1 (float): The first number to be summed.
    - num2 (float): The second number to be summed.

    Returns:
    - float: The sum of the two numbers.

    Example:
    >>> sum_numbers(1.5, 3.5)
    5.0
    >>> sum_numbers(2.2, 5.3)
    7.5
    """
    return num1 + num2


print(f"Sum = {sum_numbers(1.7, 3.8)}")
```

[Повернутися до змісту](#зміст-уроку)

---

## 4. Анотації типів `Annotation types`

> 💡 **Анотація типів** - це механізм, що дозволяє **вказувати** очікувані типи даних для **змінних**, **параметрів**
> функцій або **значень**, які функція повертає.

- Анотації типів сприяють підвищенню **читабельності** коду, полегшують його **налаштування** та дозволяють інструментам
  статичного аналізу виконувати перевірку вашого коду на потенційні помилки.
- `PEP 8` - це офіційний документ, який описує стиль написання коду на мові програмування Python та містить рекомендації
  щодо форматування коду, щоб зробити код більш читабельним і послідовним.
- Застосування анотацій типів не впливає на час виконання програми, оскільки **Python** залишається **динамічно**
  типізованою мовою програмування.

> 💡 **Анотація** простих типів дозволяє вказати **очікуваний** тип даних для **змінних** або **аргументів** функцій.

Для базових типів (`int`, `float`, `str`, `bool`) анотація виглядає як **пряме визначення** типу.

```python
# Анотація параметрів функції
def greet(name: str, age: int) -> str:
    return f"Hello, {name}. You are {age} years old."


# Анотація змінних
name: str = "John"
age: int = 17

# Виклик функції
print(greet(name, age))
```

> 💡 Анотації для колекцій імпортуються з модуля `typing`, який дозволяє вказувати тип елементів, що містить колекція.

```python
from typing import List, Dict, Set, Tuple

names: List[str] = ["Alice", "Bob", "Charlie"]
scores: Dict[str, int] = {"Alice": 10, "Bob": 15, "Charlie": 8}
unique_numbers: Set[int] = {1, 2, 3, 4}
coordinates: Tuple[int] = (10, -2, 0)
```

💡 Пояснення:

- `List[str]` - **список**, що містить **рядки**.
- `Dict[str, int]` - **словник**, ключами якого є **рядки**, а значеннями - **цілі** числа.
- `Set[int]` - **множина**, що містить **цілі** числа.
- `Tuple[int]` - **кортеж**, що містить **цілі** числа.

### Модуль `typing` також надає інші корисні класи для анотацій типів:

- `Union`
- `Optional`
- `Any`
- `Callable`

### 💡 `Union[x, y]`:

- **Union** використовується, коли значення може бути одним з декількох конкретних типів (`x` або `y`).
- Використання **Union** корисно, коли функція може **приймати** або **повертати** дані **різних типів**.

```python
# Імпортуємо Union з модуля typing
from typing import Union


# Функція process_input приймає один аргумент, який може бути або цілим числом (int), або рядком (str)
def process_input(value: Union[int, str]) -> Union[int, str]:
    # Перевіряємо, чи є значення цілим числом
    if isinstance(value, int):
        # Якщо так, повертаємо рядок з інформацією про число
        return f"Number: {value}"
    else:
        # Якщо ні, повертаємо рядок з інформацією про текст
        return f"Text: {value}"
```

### 💡 `Optional[x]`:

- **Optional** еквівалентний `Union[x, None]` та призначений для випадків, коли значення може бути `None`.

- Використання **Optional** корисно, коли функція або метод може повертати `None` замість конкретного значення.

- `None` - це об'єкт типу `NoneType`, який використовується для представлення **відсутності** значення.

- `None` часто вказує на те, що **змінна** не була **ініціалізована** або **функція** не повернула жодного **значення**.

```python
# Імпортуємо Optional з модуля typing
from typing import Optional


# Функція get_name приймає один аргумент user_id типу int
# Функція повертає значення типу Optional[str], що означає, що вона може повернути або рядок (str), або None
def get_name(user_id: int) -> Optional[str]:
    # Створюємо словник користувачів, де ключі - це ідентифікатори користувачів, а значення - їхні імена
    users = {1: "Alice", 2: "Bob"}
    # Використовуємо метод get для отримання імені користувача за його ідентифікатором
    # Якщо користувач з таким ідентифікатором не знайдений, метод get поверне None
    return users.get(user_id)


print(get_name(1))
print(get_name(3))
```

### 💡 `Any`:

**Any** використовується коли тип даних **невідомий** або може бути **будь-яким**.

```python
# Імпортуємо Any з модуля typing
from typing import Any


# Функція log_value приймає один аргумент value, який може бути будь-якого типу (Any)
# Функція також повертає значення типу Any, що означає, що вона може повернути будь-який тип
def log_value(value: Any) -> Any:
    # Виводимо значення аргументу value на екран у форматі рядка
    print(f"Some value: {value}")
```

### 💡 `Callable`:

**Callable** використовується для **анотації функцій**, які приймають **інші функції** як **аргументи**.

```python
# Імпортуємо Callable з модуля typing
from typing import Callable


# Функція, яка використовує анотацію Callable
def apply_function(func: Callable, a: int, b: int) -> int:
    """
    Функція apply_function приймає іншу функцію та 2 цілих числа як аргументи.

    Parameters:
    - func (Callable[[int, int], int]): Функція, яка буде викликана з двома аргументами.
    - a (int): Перше ціле число, яке буде передане у функцію.
    - b (int): Друге ціле число, яке буде передане у функцію.
    """
    return func(a, b)


# Визначаємо функцію add, яка приймає два цілих числа та повертає їх суму
def add(x: int, y: int) -> int:
    return x + y


# Створюємо змінні num1 і num2
num1 = 3
num2 = 4

# Викликаємо функцію apply_function, передаючи функцію add та змінні num1 і num2
print(apply_function(add, num1, num2))

```

[Повернутися до змісту](#зміст-уроку)

---

## 5. Реалізація `docstring`

Необхідно додати `docstring`, з описом **вхідних аргументів** та **функцій** проєкту **TelegramBot**.

Необхідно **видалити власні** коментарі, які ми створили та використовувати на попередніх заняттях.

```python
import asyncio
import logging
import sys

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
    """Клас, що визначає стани для отримання інформації про фільм."""
    name = State()
    description = State()
    rating = State()
    genre = State()
    actors = State()
    poster = State()


class FilmStates(StatesGroup):
    """Клас, що визначає стани для різних операцій з фільмами."""
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
    Обробник для команди /start.
    Функція відправляє вітальне повідомлення користувачу.

    Аргументи:
        message (Message): Повідомлення від користувача.
    """
    await message.answer(
        f"Hello🖐, {html.bold(message.from_user.full_name)}!\n"
        "I'm your first Telegram Bot 🥳"
    )


@dp.message(FILMS_COMMAND)
@async_log_function
async def films(message: Message) -> None:
    """
    Обробник для команди /films.
    Функція відправляє список фільмів користувачу.

    Аргументи:
        message (Message): Повідомлення від користувача.
    """
    data = get_films()
    markup = films_keyboard_markup(films_list=data)
    await message.answer(
        f"<b>Список фільмів: 🎬</b>\nОберіть фільм, щоб отримати інформацію про нього.",
        reply_markup=markup
    )


@dp.callback_query(FilmCallback.filter())
@async_log_function
async def callback_film(callback: CallbackQuery, callback_data: FilmCallback) -> None:
    """
    Обробник зворотного виклику для фільмів.
    Функція відправляє детальну інформацію про вибраний фільм.

    Аргументи:
        callback (CallbackQuery): Зворотний виклик від користувача.
        Callback_data (FilmCallback): Дані зворотного виклику.
    """
    film_id = callback_data.id
    film_data = get_films(film_id=film_id)
    film = Film(**film_data)
    text = (
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


@dp.message(FILM_CREATE_COMMAND)
@async_log_function
async def film_create(message: Message, state: FSMContext) -> None:
    """
    Початок процесу створення нового фільму.
    Функція запитує назву фільму в користувача.

    Аргументи:
        message (Message): Повідомлення від користувача.
        State (FSMContext): Контекст стану для керування станом діалогу.
    """
    await state.set_state(FilmForm.name)
    await message.answer(
        f"<b>Введіть назву фільму ...</b>",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(FilmForm.name)
@async_log_function
async def film_name(message: Message, state: FSMContext) -> None:
    """
    Функція отримує назву фільму та запитує опис фільму.

    Аргументи:
        message (Message): Повідомлення від користувача.
        State (FSMContext): Контекст стану для керування станом діалогу.
    """
    await state.update_data(name=message.text)
    await state.set_state(FilmForm.description)
    await message.answer(
        f"<b>Введіть опис фільму ...</b>",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(FilmForm.description)
@async_log_function
async def film_description(message: Message, state: FSMContext) -> None:
    """
    Функція отримує опис фільму та запитує рейтинг фільму.

    Аргументи:
        message (Message): Повідомлення від користувача.
        State (FSMContext): Контекст стану для керування станом діалогу.
    """
    await state.update_data(description=message.text)
    await state.set_state(FilmForm.rating)
    await message.answer(
        f"<b>Вкажіть рейтинг фільму (від 0 до 10) ...</b>",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(FilmForm.rating)
@async_log_function
async def film_rating(message: Message, state: FSMContext) -> None:
    """
    Функція отримує рейтинг фільму та запитує жанр фільму.

    Аргументи:
        message (Message): Повідомлення від користувача.
        State (FSMContext): Контекст стану для керування станом діалогу.
    """
    await state.update_data(rating=float(message.text))
    await state.set_state(FilmForm.genre)
    await message.answer(
        f"<b>Введіть жанр фільму ...</b>",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(FilmForm.genre)
@async_log_function
async def film_genre(message: Message, state: FSMContext) -> None:
    """
    Функція отримує жанр фільму та запитує акторів фільму.

    Аргументи:
        message (Message): Повідомлення від користувача.
        State (FSMContext): Контекст стану для керування станом діалогу.
    """
    await state.update_data(genre=message.text)
    await state.set_state(FilmForm.actors)
    await message.answer(
        text=f"<b>Введіть акторів фільму через `, ` \n⚠️ (Обов'язкова кома та відступ після неї)</b>",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(FilmForm.actors)
@async_log_function
async def film_actors(message: Message, state: FSMContext) -> None:
    """
    Функція отримує акторів фільму та запитує посилання на постер фільму.

    Аргументи:
        message (Message): Повідомлення від користувача.
        State (FSMContext): Контекст стану для керування станом діалогу.
    """
    await state.update_data(actors=[x for x in message.text.split(", ")])
    await state.set_state(FilmForm.poster)
    await message.answer(
        f"<b>Введіть посилання на постер фільму ...</b>",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(FilmForm.poster)
@async_log_function
async def film_poster(message: Message, state: FSMContext) -> None:
    """
    Функція отримує посилання на постер фільму та завершує процес створення фільму.

    Аргументи:
        message (Message): Повідомлення від користувача.
        State (FSMContext): Контекст стану для керування станом діалогу.
    """
    data = await state.update_data(poster=message.text)
    film = Film(**data)
    add_film(film.model_dump())
    await state.clear()
    await message.answer(
        f"<b>Фільм {film.name} успішно додано ✅</b>",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(Command("search_film"))
async def search_film(message: Message, state: FSMContext):
    """
    Початок процесу пошуку фільму за назвою.

    Аргументи:
        message (Message): Повідомлення від користувача.
        State (FSMContext): Контекст стану для керування станом діалогу.
    """
    await state.set_state(FilmStates.search_query)
    await message.reply("<b>Введіть назву фільму для пошуку:</b>")


@dp.message(FilmStates.search_query)
@async_log_function
async def get_search_query(message: Message, state: FSMContext):
    """
    Функція отримує назву фільму для пошуку та відправляє результати пошуку.

    Аргументи:
        message (Message): Повідомлення від користувача.
        State (FSMContext): Контекст стану для керування станом діалогу.
    """
    query = message.text.lower()
    films_data = get_films()
    results = [film for film in films_data if query in film['name'].lower()]
    if results:
        for film_data in results:
            film = Film(**film_data)
            text = (f"<b>Фільм:</b> {film.name}\n"
                    f"<b>Опис:</b> {film.description}\n"
                    f"<b>Рейтинг:</b> {film.rating}\n"
                    f"<b>Жанр:</b> {film.genre}\n"
                    f"<b>Актори:</b> {', '.join(film.actors)}\n")
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
async def filter_film(message: Message, state: FSMContext):
    """
    Початок процесу фільтрації фільмів за жанром.

    Аргументи:
        message (Message): Повідомлення від користувача.
        State (FSMContext): Контекст стану для керування станом діалогу.
    """
    await state.set_state(FilmStates.filter_criteria)
    await message.reply("<b>Введіть жанр фільму для фільтрації:</b>")


@dp.message(FilmStates.filter_criteria)
@async_log_function
async def get_filter_criteria(message: Message, state: FSMContext):
    """
    Функція отримує жанр фільму для фільтрації та відправляє відфільтровані результати.

    Аргументи:
        message (Message): Повідомлення від користувача.
        State (FSMContext): Контекст стану для керування станом діалогу.
    """
    criteria = message.text.lower()
    films_data = get_films()
    filtered = list(filter(
        lambda film: criteria in film['genre'].lower(),
        films_data
    ))
    if filtered:
        for film_data in filtered:
            film = Film(**film_data)
            text = (f"<b>Фільм:</b> {film.name}\n"
                    f"<b>Опис:</b> {film.description}\n"
                    f"<b>Рейтинг:</b> {film.rating}\n"
                    f"<b>Жанр:</b> {film.genre}\n"
                    f"<b>Актори:</b> {', '.join(film.actors)}\n")
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
async def delete_film(message: Message, state: FSMContext):
    """
    Початок процесу видалення фільму за назвою.

    Аргументи:
        message (Message): Повідомлення від користувача.
        State (FSMContext): Контекст стану для керування станом діалогу.
    """
    await message.reply("<b>Введіть назву фільму, який бажаєте видалити:</b>")
    await state.set_state(FilmStates.delete_query)


@dp.message(FilmStates.delete_query)
@async_log_function
async def get_delete_query(message: Message, state: FSMContext):
    """
    Функція отримує назву фільму для видалення та видаляє фільм.

    Аргументи:
        message (Message): Повідомлення від користувача.
        State (FSMContext): Контекст стану для керування станом діалогу.
    """
    film_to_delete = message.text.lower()
    films_data = get_films()
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
async def edit_film(message: Message, state: FSMContext):
    """
    Початок процесу редагування інформації про фільм.

    Аргументи:
        message (Message): Повідомлення від користувача.
        State (FSMContext): Контекст стану для керування станом діалогу.
    """
    films_data = get_films()
    if not films_data:
        await message.reply("<b>Список фільмів порожній. Немає що редагувати.</b>")
        return
    film_names = "\n".join([f"- {film['name']}" for film in films_data])
    await message.reply(
        "<b>Введіть назву фільму, який бажаєте редагувати:</b>\n"
        f"Доступні фільми:\n{film_names}"
    )
    await state.set_state(FilmStates.edit_query)


@dp.message(FilmStates.edit_query)
@async_log_function
async def get_edit_query(message: Message, state: FSMContext):
    """
    Функція отримує назву фільму для редагування та запитує поле для редагування.

    Аргументи:
        message (Message): Повідомлення від користувача.
        State (FSMContext): Контекст стану для керування станом діалогу.
    """
    film_name = message.text.strip()
    films_data = get_films()
    film_found = None
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
async def process_edit(message: Message, state: FSMContext):
    """
    Функція отримує поле та нове значення для редагування фільму та оновлює інформацію.

    Аргументи:
        message (Message): Повідомлення від користувача.
        State (FSMContext): Контекст стану для керування станом діалогу.
    """
    try:
        data = await state.get_data()
        film = data['film']
        films_data = data['films_data']
        if '|' not in message.text:
            raise ValueError("Невірний формат. Використовуйте '|' для розділення поля та значення")
        field, new_value = message.text.split('|', 1)
        field = field.strip().lower()
        new_value = new_value.strip()
        valid_fields = ['name', 'description', 'rating', 'genre', 'actors', 'poster']
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
        await message.reply(f"<b>Фільм '{film['name']}' успішно оновлено!</b>\n"
                            f"<b>{field}:</b> {new_value}")
        await state.clear()
    except Exception as e:
        await message.reply(f"<b>Помилка:</b> {str(e)}\n"
                            "<b>Використовуйте формат:</b>\n"
                            "<code>поле|нове значення</code>\n"
                            "<b>Приклад:</b> <code>rating|9.5</code>")
        await state.clear()


@dp.message(Command("recommend_film"))
@async_log_function
async def recommend_film(message: Message) -> None:
    """
    Функція рекомендує фільми з найвищим рейтингом.

    Аргументи:
        message (Message): Повідомлення від користувача.
    """
    films_data = get_films()
    rated_films = [film for film in films_data if film.get('rating') is not None]
    if not rated_films:
        await message.reply("<b>На жаль, немає фільмів з рейтингом для рекомендації.</b>")
        return
    top_films = sorted(rated_films, key=lambda x: float(x['rating']), reverse=True)[:3]
    await message.reply("<b>🍿 Best ⭐️ Films:</b>")
    for i, film_data in enumerate(top_films, 1):
        film = Film(**film_data)
        text = (f"<b>#{i} Рекомендований фільм:</b>\n"
                f"<b>Назва:</b> {film.name}\n"
                f"<b>Опис:</b> {film.description}\n"
                f"<b>Рейтинг:</b> ⭐️ {film.rating}/10\n"
                f"<b>Жанр:</b> {film.genre}\n"
                f"<b>Актори:</b> {', '.join(film.actors)}\n")
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
    Головна асинхронна функція для запуску бота.
    Ініціалізує бота та запускає цикл опитування для отримання оновлень.
    """
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.set_my_commands(BOT_COMMANDS)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
```

[Повернутися до змісту](#зміст-уроку)

---

## 6. Реалізація `Annotation types`

Необхідно перевірити/додати **анотації типів** у функції проєкту **TelegramBot**.

Імпортуємо необхідні **анотації** типів з модуля `typing`:

```python
from typing import List, Dict, Any, Optional, Tuple
```

💡 Також, **good practice** вважається відсутність інших мов у коді застосунку, окрім **англійської** мови, тому
перекладемо `docstrings` на англійську мову.

```python
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
    await message.answer(
        f"Hello🖐, {html.bold(message.from_user.full_name)}!\n"
        "I'm your first Telegram Bot 🥳"
    )


@dp.message(FILMS_COMMAND)
@async_log_function
async def films(message: Message) -> None:
    """
    Handler for the /films command.
    The function sends a list of films to the user.

    Arguments:
        message (Message): Message from the user.
    """
    data = get_films()
    markup = films_keyboard_markup(films_list=data)
    await message.answer(
        f"<b>Список фільмів: 🎬</b>\nОберіть фільм, щоб отримати інформацію про нього.",
        reply_markup=markup
    )


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
    await state.set_state(FilmForm.name)
    await message.answer(
        f"<b>Введіть назву фільму ...</b>",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(FilmForm.name)
@async_log_function
async def film_name(message: Message, state: FSMContext) -> None:
    """
    The function receives the film name and asks for the film description.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    await state.update_data(name=message.text)
    await state.set_state(FilmForm.description)
    await message.answer(
        f"<b>Введіть опис фільму ...</b>",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(FilmForm.description)
@async_log_function
async def film_description(message: Message, state: FSMContext) -> None:
    """
    The function receives the film description and asks for the film rating.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    await state.update_data(description=message.text)
    await state.set_state(FilmForm.rating)
    await message.answer(
        f"<b>Вкажіть рейтинг фільму (від 0 до 10) ...</b>",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(FilmForm.rating)
@async_log_function
async def film_rating(message: Message, state: FSMContext) -> None:
    """
    The function receives the film rating and asks for the film genre.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    await state.update_data(rating=float(message.text))
    await state.set_state(FilmForm.genre)
    await message.answer(
        f"<b>Введіть жанр фільму ...</b>",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(FilmForm.genre)
@async_log_function
async def film_genre(message: Message, state: FSMContext) -> None:
    """
    The function receives the film genre and asks for the film actors.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    await state.update_data(genre=message.text)
    await state.set_state(FilmForm.actors)
    await message.answer(
        text=f"<b>Введіть акторів фільму через `, ` \n⚠️ (Обов'язкова кома та відступ після неї)</b>",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(FilmForm.actors)
@async_log_function
async def film_actors(message: Message, state: FSMContext) -> None:
    """
    The function receives the film actors and asks for the film poster link.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    await state.update_data(actors=[x for x in message.text.split(", ")])
    await state.set_state(FilmForm.poster)
    await message.answer(
        f"<b>Введіть посилання на постер фільму ...</b>",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(FilmForm.poster)
@async_log_function
async def film_poster(message: Message, state: FSMContext) -> None:
    """
    The function receives the film poster link and completes the film creation process.

    Arguments:
        message (Message): Message from the user.
        state (FSMContext): State context for managing dialog state.
    """
    data: Dict[str, Any] = await state.update_data(poster=message.text)
    film: Film = Film(**data)
    add_film(film.model_dump())
    await state.clear()
    await message.answer(
        f"<b>Фільм {film.name} успішно додано ✅</b>",
        reply_markup=ReplyKeyboardRemove(),
    )


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
    bot: Bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.set_my_commands(BOT_COMMANDS)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
```

[Повернутися до змісту](#зміст-уроку)

---

## 7. Реалізація `Exception Handling`

Необхідно перевірити/додати **exception handling** у функціях проєкту **TelegramBot**.

```python
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
```

[Повернутися до змісту](#зміст-уроку)

---

## 8. Реалізація `Testing`

Необхідно додати **тести**, які будуть виконувати перевірку базових функцій проєкту **TelegramBot**.

- Створити package `tests` в корені проєкту, з модулями `test_bot.py` та `__init__.py` всередині.
- Додати наступний код в модуль `__init__.py`:

```python
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
```

Інсталювати бібліотеки `pytest` та `pytest-asyncio`

```text
pip install pytest pytest-asyncio
```

Оновити файл `requirements.txt`

```text
pip freeze > requirements.txt
```

Додати наступний код до файлу `test_bot.py`

```python
import pytest
import pytest_asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from aiogram.types import Message, User, CallbackQuery
from aiogram.fsm.context import FSMContext
from bot import (
    start, films, film_create, search_film, recommend_film,
    callback_film, film_name, film_description, film_rating
)


class TestTelegramBot:
    @pytest_asyncio.fixture
    async def message(self):
        """Fixture для створення базового message об'єкта"""
        message = MagicMock(spec=Message)
        message.answer = AsyncMock()
        message.reply = AsyncMock()
        message.from_user = MagicMock(spec=User)
        message.from_user.full_name = "Test User"
        return message

    @pytest_asyncio.fixture
    async def state(self):
        """Fixture для створення FSMContext"""
        state = MagicMock(spec=FSMContext)
        state.set_state = AsyncMock()
        state.update_data = AsyncMock()
        return state

    @pytest.mark.asyncio
    async def test_start_command(self, message):
        """Test start command handler"""
        # Act
        await start(message)

        # Assert
        message.answer.assert_called_once()
        args = message.answer.call_args[0][0]
        assert "Hello" in args
        assert "Test User" in args

    @pytest.mark.asyncio
    async def test_films_command(self, message):
        """Test films command handler"""
        # Arrange
        test_films = [
            {"name": "Test Film", "description": "Test Description", "rating": 8.0}
        ]

        with patch('bot.get_films', return_value=test_films):
            await films(message)
            message.answer.assert_called_once()
            args = message.answer.call_args[0][0]
            assert "Список фільмів" in args

    @pytest.mark.asyncio
    async def test_film_create_command(self, message, state):
        """Test film creation start handler"""
        await film_create(message, state)
        state.set_state.assert_called_once()
        message.answer.assert_called_once()
        args = message.answer.call_args[0][0]
        assert "Введіть назву фільму" in args

    @pytest.mark.asyncio
    async def test_search_film_start(self, message, state):
        """Test search film command initialization"""
        await search_film(message, state)
        state.set_state.assert_called_once()
        message.reply.assert_called_once()
        args = message.reply.call_args[0][0]
        assert "Введіть назву фільму для пошуку" in args

    @pytest.mark.asyncio
    async def test_recommend_film_no_films(self, message):
        """Test recommend_film handler when no films available"""
        with patch('bot.get_films', return_value=[]):
            await recommend_film(message)
            message.reply.assert_called_once()
            args = message.reply.call_args[0][0]
            assert "На жаль, немає фільмів" in args

    @pytest.mark.asyncio
    async def test_callback_film(self):
        """Test callback handler for film details"""
        callback = MagicMock(spec=CallbackQuery)
        callback.message = MagicMock(spec=Message)
        callback.message.answer_photo = AsyncMock()
        callback_data = MagicMock()
        callback_data.id = 1
        test_film = {
            "name": "Test Film",
            "description": "Test Description",
            "rating": 8.0,
            "genre": "Action",
            "actors": ["Actor 1", "Actor 2"],
            "poster": "http://example.com/poster.jpg"
        }
        with patch('bot.get_films', return_value=test_film):
            await callback_film(callback, callback_data)
            callback.message.answer_photo.assert_called_once()
            caption = callback.message.answer_photo.call_args[1]['caption']
            assert "Test Film" in caption
            assert "Test Description" in caption

    @pytest.mark.asyncio
    async def test_film_name_handler(self, message, state):
        """Test handling film name input"""
        message.text = "Test Film Name"
        await film_name(message, state)
        state.update_data.assert_called_once_with(name="Test Film Name")
        state.set_state.assert_called_once()
        message.answer.assert_called_once()
        assert "опис фільму" in message.answer.call_args[0][0].lower()

    @pytest.mark.asyncio
    async def test_film_description_handler(self, message, state):
        """Test handling film description input"""
        message.text = "Test Description"
        await film_description(message, state)
        state.update_data.assert_called_once_with(description="Test Description")
        state.set_state.assert_called_once()
        message.answer.assert_called_once()
        assert "рейтинг" in message.answer.call_args[0][0].lower()

    @pytest.mark.asyncio
    async def test_film_rating_handler_valid(self, message, state):
        """Test handling valid film rating input"""
        message.text = "8.5"
        await film_rating(message, state)
        state.update_data.assert_called_once_with(rating=8.5)
        state.set_state.assert_called_once()
        message.answer.assert_called_once()
        assert "жанр" in message.answer.call_args[0][0].lower()
```

Виконати тести можна запустивши файл `test_bot.py` або за допомогою наступної команди:

```text
pytest tests/test_bot.py
```

### 🧩 Test Coverage:

Для перевірки відсотка покриття тестами у вашому проєкті можна використати `pytest` разом з `pytest-cov`.

Необхідно встановити бібліотеку `pytest-cov`:

```text
pip install pytest-cov
```

Необхідно запустити тести з наступними параметрами для перевірки покриття.

```text
# Базовий варіант (показує загальний відсоток покриття)
pytest --cov=bot tests/
```

[Повернутися до змісту](#зміст-уроку)

---

## 9. Підведення підсумків 🚀

> На цьому уроці ми вивчили та повторили наступні теми:

- Стиль коду. `PEP 8`. Рефакторинг коду
- Documentation String (`Docstring`)
- Анотації типів (`Annotation types`)
- Реалізація `Docstring`
- Реалізація `Annotation types`
- Реалізація `Exception Handling`
- Реалізація `Testing`

[Повернутися до змісту](#зміст-уроку)

---

## 10. Домашнє завдання 🏠

### 🧩 Завдання:

Необхідно організувати код проєкту та виконати тестування всіх складових.

### Додаткові завдання для збільшення можливостей проекту:

1. Персоналізація: Дозволити користувачам створювати власні списки улюблених фільмів, оцінювати фільми та отримувати
   персоналізовані рекомендації.
2. Інтеграція з зовнішніми сервісами: Інтегрувати бота з кінобазами даних (IMDb) для отримання більш
   детальної інформації про фільми.
3. Оптимізація: Оптимізувати код для підвищення швидкодії та ефективності бота.
4. Розгортання: Розгорнути бота на хостингу, щоб зробити його доступним для широкого кола користувачів.

[Повернутися до змісту](#зміст-уроку)

---