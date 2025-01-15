import argparse
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()


def hello_argparse() -> None:
    # Создание парсера
    parser = argparse.ArgumentParser(
        description="Пример использования позиционных и опциональных аргументов",
    )
    # Определение позиционного аргумента
    parser.add_argument(
        "name",
        type=str,
        help="Имя пользователя (обязательно)",
    )
    # Определение опциональных аргументов
    parser.add_argument(
        "--age",
        type=int,
        default=18,
        help="Возраст пользователя (по умолчанию: 18)",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Включить режим отладки",
    )
    # Парсинг аргументов командной строки
    args = parser.parse_args()

    # Обработка аргументов
    logger.info(f"Привет, {args.name}!")  # Позиционный аргумент
    logger.info(f"Возраст {args.age} лет.")  # Опциональный аргумент (значение по умолчанию)
    if args.debug:  # Флаг
        logger.info("Режим отладки включен.")


if __name__ == "__main__":
    hello_argparse()


# Примеры вызова из командной строки:
# python passing_arguments_argparce.py John
# python passing_arguments_argparce.py John --age 25
# python passing_arguments_argparce.py John --debug
# python passing_arguments_argparce.py John --age 30 --debug
# python passing_arguments_argparce.py John --debug --age 30
# python passing_arguments_argparce.py John --help
# Ошибочные вызовы:
# python passing_arguments_argparce.py
