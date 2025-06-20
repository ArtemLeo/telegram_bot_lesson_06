import logging
from functools import wraps
from typing import Callable, Any

# Налаштування логування
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Форматування повідомлень логування
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Обробник для запису логів у файл
file_handler = logging.FileHandler('logger_journal.log', mode='a')
file_handler.setFormatter(formatter)

# Обробник для виведення логів у консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Додавання обробників до логера
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def async_log_function(func: Callable) -> Callable:
    """Декоратор для логування викликів асинхронних функцій."""

    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        logger.info(f"Виклик функції '{func.__name__}' з аргументами: {args}, {kwargs}")
        try:
            result = await func(*args, **kwargs)
            logger.info(f"Функція '{func.__name__}' успішно завершила роботу")
            return result
        except Exception as e:
            logger.error(f"Помилка у функції '{func.__name__}': {e}", exc_info=True)
            raise

    return wrapper
