import argparse
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()


def main() -> None:
    parser = argparse.ArgumentParser(description="Пример позиционирования аргументов и опций")

    # Позиционный аргумент 'name'
    parser.add_argument("name", type=str, help="Имя пользователя")

    # Позиционный аргумент 'age' (необязательный, но требует одного значения)
    parser.add_argument("age", type=int, nargs="?", help="Возраст пользователя")

    # Позиционный аргумент c множественным количеством значений (nargs='+')
    parser.add_argument("files", type=str, nargs="+", help="Список файлов для обработки")

    # Опция c дефолтным значением
    parser.add_argument("--email", type=str, help="Email пользователя", default=None)

    # Опция, которая может быть использована несколько раз (multiple)
    parser.add_argument("--tags", type=str, help="Теги", action="append")

    # Опция c несколькими значениями (nargs='*')
    parser.add_argument("--dirs", type=str, nargs="*", help="Список директорий", default=[])

    args = parser.parse_args()

    # Вывод полученных значений
    logger.info(f"Имя: {args.name}")
    if args.age is not None:
        logger.info(f"Возраст: {args.age}")
    logger.info(f"Файлы: {', '.join(args.files)}")
    if args.email:
        logger.info(f"Email: {args.email}")
    if args.tags:
        logger.info(f"Теги: {', '.join(args.tags)}")
    else:
        logger.info("Теги: не указаны")
    if args.dirs:
        logger.info(f"Директории: {', '.join(args.dirs)}")
    else:
        logger.info("Директории: не указаны")


if __name__ == "__main__":
    main()

# Примеры вызова из командной строки:
# python positioning_arguments_argparce.py John 30 file1.txt file2.txt --email john@example.com --dirs dir1 dir2
# python positioning_arguments_argparce.py John 30 file1.txt
# python positioning_arguments_argparce.py John 30 1.txt 2.txt --email john@example.com --tags tag1 --tags tag2 --tags tag3

# Нюансы:
# nargs='+' в files — это позиционный аргумент, который требует одного или более значений. Команда будет требовать хотя бы одно значение для этого аргумента
# nargs='*' в dirs — это опция, которая может принимать любое количество значений, включая 0
# nargs='?' позволяет сделать аргумент необязательным
# Когда используется action="append" для опций, это позволяет собирать все значения, переданные для одной опции, в список
