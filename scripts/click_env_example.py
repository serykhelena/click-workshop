import logging
import os

import click

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@click.command(help="Пример использования переменной среды в опции")
@click.option("--username", envvar="USERNAME", help="Имя, задано через переменную среды USERNAME")
def greet(username):
    """
    Приветствие пользователя c использованием имени из переменной среды.
    """
    if username:
        click.echo(f"Привет, {username}!")
    else:
        click.echo("Привет, незнакомец!")


@click.group()
@click.pass_context
def cli(ctx):
    """
    Главная группа команд. Загружает переменные среды в контекст.
    """
    # Инициализируем словарь для хранения переменных среды
    ctx.ensure_object(dict)

    # Загружаем переменные среды (например, из os.environ)
    ctx.obj["env"] = {key: os.getenv(key) for key in os.environ}


@cli.command("show-env", help="Показать загруженные переменные среды")
@click.pass_context
def show_env(ctx):
    """
    Показать все загруженные переменные среды.
    """
    logger.info("Текущие переменные среды:")
    for key, value in ctx.obj["env"].items():
        logger.info(f"{key}: {value}")


@cli.command("add-env", help="Добавить новую переменную среды")
@click.argument("key", type=str)
@click.argument("value", type=str)
@click.pass_context
def add_env(ctx, key, value):
    """
    Добавить новую переменную в контекст и системные переменные среды.
    """
    # Добавляем переменную в контекст
    ctx.obj["env"][key] = value

    # Опционально: добавляем в os.environ (будет доступно только в процессе выполнения)
    os.environ[key] = value

    logger.info(f"Переменная среды '{key}' добавлена c значением '{value}'.")

    logger.info("Текущие переменные среды:")
    for key_for, value_for in ctx.obj["env"].items():
        logger.info(f"{key_for}: {value_for}")


if __name__ == "__main__":
    cli.add_command(greet)
    cli()


# Примеры вызова из командной строки:
# python click_env_example.py show-env
# python click_env_example.py add-env NEW_VAR test_value
#       $env:USERNAME="John"
#       python click_env_example.py greet

# Нюансы:
# ctx.ensure_object(dict): Инициализация объекта контекста, который используется для хранения
#   состояния между командами
# Можно сохранять и загружать данные через локальный env
# Работа c os.environ: Переменные можно загружать из текущей среды и добавлять их в
#   процессе выполнения
