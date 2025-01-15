import logging

import click

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@click.group()
def cli():
    """
    Основная группа команд.
    """


@click.command()
@click.argument("name", type=str)
@click.argument("age", type=int)
def add(name, age):
    """
    Команда для добавления нового пользователя.
    """
    logger.info(f"Добавление пользователя: {name}, возраст: {age}")


@click.command()
@click.argument("user_id", type=int)
def delete(user_id):
    """
    Команда для удаления пользователя.
    """
    logger.info(f"Удаление пользователя c ID: {user_id}")


# Добавляем команды в группу
cli.add_command(add)
cli.add_command(delete)

if __name__ == "__main__":
    cli()

# Примеры вызова из командной строки:
# python group_commands_click.py add John 30
# python group_commands_click.py delete 101
