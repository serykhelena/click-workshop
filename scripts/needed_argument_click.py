import click


@click.command()
# Позиционный обязательный аргумент name
@click.argument("name", type=str)
# Позиционный необязательный аргумент age (принимает любое число значений)
@click.argument("age", type=int, nargs=-1)
# Опция email (необязательная)
@click.option("--email", type=str)
# Опция id_user (обязательная)
@click.option("--id_user", type=int, required=True)
def process_files(name: str, age: int | None, email: str | None, id_user: int) -> None:
    """Обрабатываем несколько файлов."""
    click.echo(f"Имя: {name}")
    click.echo(f"id пользователя: {id_user}")
    if age:
        click.echo(f"Возраст: {age}")
    if email:
        click.echo(f"Email: {email}")


if __name__ == "__main__":
    process_files()

# Примеры запуска:
# python needed_argument_click.py John --id_user 101
# python needed_argument_click.py John --id_user 101 --age 30
# python needed_argument_click.py John 30 40 --id_user 101      (странный пример :) )
# python needed_argument_click.py John --id_user 101 --email=@abc.com
# Нюансы:
# Аргументы:
#   По умолчанию обязательные.
#   Можно сделать их необязательными c помощью nargs (например, nargs=-1 для нескольких значений).
# Опции:
#   По умолчанию необязательные.
#   Можно сделать обязательными c помощью required=True.
#   Можно задать значение по умолчанию c помощью default.
#   Можно передавать несколько значений c помощью multiple=True или nargs=-1.
