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
        """Fixture for creating a basic message object"""
        message = MagicMock(spec=Message)
        message.answer = AsyncMock()
        message.reply = AsyncMock()
        message.from_user = MagicMock(spec=User)
        message.from_user.full_name = "Test User"
        return message

    @pytest_asyncio.fixture
    async def state(self):
        """Fixture for creating an FSMContext"""
        state = MagicMock(spec=FSMContext)
        state.set_state = AsyncMock()
        state.update_data = AsyncMock()
        return state

    @pytest.mark.asyncio
    async def test_start_command(self, message):
        """Test start command handler"""
        await start(message)
        message.answer.assert_called_once()
        args = message.answer.call_args[0][0]
        assert "Hello" in args
        assert "Test User" in args

    @pytest.mark.asyncio
    async def test_films_command(self, message):
        """Test films command handler"""
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
