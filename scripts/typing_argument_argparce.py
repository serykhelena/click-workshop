import argparse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def comma_separated_list(value: str) -> list[str]:
    """
    Пример пользовательской функции для преобразования строкового аргумента
    в список, разделённый запятыми.
    """
    try:
        return value.split(",")
    except Exception:
        msg = f"'{value}' не является корректным списком через запятую"
        raise argparse.ArgumentTypeError(msg) from None


def main():
    parser = argparse.ArgumentParser(description="Пример типизации c argparse")

    # Стандартные типы
    parser.add_argument("name", type=str, help="Имя пользователя (строка)")
    parser.add_argument("age", type=int, help="Возраст пользователя (целое число)")
    parser.add_argument(
        "--pi",
        type=float,
        default=3.14,
        help="Произвольное число c плавающей точкой (по умолчанию: 3.14)",
    )
    parser.add_argument("--optional", help="Опциональный аргумент без указанного типа")

    # Кастомные функции типизации
    parser.add_argument("--tags", type=comma_separated_list, help="Список тегов")

    args = parser.parse_args()

    # Вывод аргументов
    logger.info(f"Имя: {args.name}")
    logger.info(f"Возраст: {args.age}")
    logger.info(f"Число π: {args.pi}")
    if args.tags:
        logger.info(f"Теги: {args.tags}")
    if args.optional:
        logger.info(f"Значение 'optional': {args.optional} (тип: {type(args.optional)})")


if __name__ == "__main__":
    main()

# Примеры вызова из командной строки:
# python typing_argument_argparce.py John 25
# python typing_argument_argparce.py John 25 --pi 3.14159
# python typing_argument_argparce.py John 25 --tags python,cli,argparse
# python typing_argument_argparce.py John 25 --optional 123

# Нюансы:
# argparse поддерживает встроенные типы Python (int, float, str, bool).
# Тип указывается в  type метода add_argument, значения автоматически приводятся к указанному типу.
# Можно использовать собственные функции для проверки и преобразования значений
# Значение type=str используется по умолчанию
