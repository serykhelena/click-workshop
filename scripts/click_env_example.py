import os

import click


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
    click.echo("Текущие переменные среды:")
    for key, value in ctx.obj["env"].items():
        click.echo(f"{key}: {value}")


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

    click.echo(f"Переменная среды '{key}' добавлена c значением '{value}'.")

    click.echo("Текущие переменные среды:")
    for key, value in ctx.obj["env"].items():  # noqa: PLR1704
        click.echo(f"{key}: {value}")


if __name__ == "__main__":
    cli()

# Примеры вызова из командной строки:
# python click_env_example.py show-env
# python click_env_example.py get-env NEW_VAR
# python click_env_example.py show-env

# Нюансы:
# ctx.ensure_object(dict): Инициализация объекта контекста, который используется для хранения
#   состояния между командами
# Работа c os.environ: Переменные можно загружать из текущей среды и добавлять их в
#   процессе выполнения
