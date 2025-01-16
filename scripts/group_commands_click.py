import logging

import click

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@click.group()
@click.option("--debug", is_flag=True, help="Включить режим отладки для всех команд")
@click.pass_context
def cli(ctx, debug):
    """
    Основная группа команд.
    """
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug
    if debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Режим отладки включен")


@click.command()
@click.argument("name", type=str)
@click.argument("age", type=int)
@click.pass_context
def add(ctx, name, age):
    """
    Команда для добавления нового пользователя.
    """
    if ctx.obj.get("DEBUG"):
        logger.debug(f"Добавление пользователя в режиме отладки: {name}, возраст: {age}")
    else:
        logger.info(f"Добавление пользователя: {name}, возраст: {age}")


@click.command()
@click.argument("user_id", type=int)
@click.pass_context
def delete(ctx, user_id):
    """
    Команда для удаления пользователя.
    """
    if ctx.obj.get("DEBUG"):
        logger.debug(f"Удаление пользователя c ID: {user_id} (режим отладки)")
    else:
        logger.info(f"Удаление пользователя c ID: {user_id}")


# Добавляем команды в группу
cli.add_command(add)
cli.add_command(delete)

if __name__ == "__main__":
    cli()


# Примеры вызова из командной строки:
# python group_commands_click.py add John 30
# python group_commands_click.py --debug  add John 30
# python group_commands_click.py delete 101
