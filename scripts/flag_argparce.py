import argparse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def main() -> None:
    parser = argparse.ArgumentParser(description="Пример работы c флагами")

    # Флаг, который активирует определенную опцию
    parser.add_argument(
        "--flag",
        action="store_true",  # Флаг, который устанавливает значение True
        help="Включить флаг",
    )

    # Парсим аргументы
    args = parser.parse_args()

    # Обработка флагов и вывод в зависимости от флагов
    if args.flag:
        logger.info("Включен флаг")
    else:
        logger.info("Флаг не включен")


if __name__ == "__main__":
    main()

# Примеры вызова из командной строки:
# python flag_argparce.py --flag
# python flag_argparce.py

# Нюансы:
# Для определения флага используется аргумент action="store_true"
