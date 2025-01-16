import argparse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def add_user(args):
    """
    Команда для добавления нового пользователя.
    """
    logger.info(f"Добавление пользователя: {args.name}, возраст: {args.age}")


def delete_user(args):
    """
    Команда для удаления пользователя.
    """
    logger.info(f"Удаление пользователя c ID: {args.user_id}")


def main():
    parser = argparse.ArgumentParser(description="Пример группировки команд c argparse")

    # Создаем парсер для подкоманд
    subparsers = parser.add_subparsers(
        title="Команды",
        description="Доступные команды",
        dest="command",
    )

    # Команда `add` для добавления пользователя
    add_parser = subparsers.add_parser("add", help="Добавить нового пользователя")
    add_parser.add_argument("name", type=str, help="Имя пользователя")
    add_parser.add_argument("age", type=int, help="Возраст пользователя")
    add_parser.set_defaults(func=add_user)

    # Команда `delete` для удаления пользователя
    delete_parser = subparsers.add_parser("delete", help="Удалить существующего пользователя")
    delete_parser.add_argument("user_id", type=int, help="ID пользователя для удаления")
    delete_parser.set_defaults(func=delete_user)

    # Парсим аргументы
    args = parser.parse_args()

    # Если команда не указана, выводим справку
    if args.command is None:
        parser.print_help()
    else:
        # Выполняем соответствующую функцию
        args.func(args)


if __name__ == "__main__":
    main()

# Примеры вызова из командной строки:
# python group_commands_argparse.py add John 30
# python group_commands_argparse.py delete 101
