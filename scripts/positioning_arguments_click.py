import click


@click.command()
@click.argument("name", type=str)
@click.argument("description", type=str, required=False)
@click.option(
    "--age",
    type=int,
    required=True,
    help="Возраст пользователя (обязательная опция).",
)
@click.option(
    "--hobbies",
    type=str,
    multiple=True,
    help="Увлечения пользователя (можно указать несколько).",
)
def greet(name: str, description: str | None, age: int, hobbies: list[str] | None) -> None:
    """
    Приветствие пользователя c указанием имени, возраста и увлечений.
    """
    click.echo(f"Привет, {name}! {age} лет.")
    if description:
        click.echo(f"Описание: {description}")
    if hobbies:
        click.echo("Твои увлечения:")
        for hobby in hobbies:
            click.echo(f"- {hobby}")
    else:
        click.echo("Нет указанных увлечений.")


if __name__ == "__main__":
    greet()

# Примеры вызова из командной строки:
# python positioning_arguments_click.py John --age 25
# python positioning_arguments_click.py John abc --age 25 --hobbies reading --hobbies traveling --hobbies coding

# Нюансы:
# required=False — делает аргумент необязательным
# multiple=True — позволяет указать опцию несколько раз
# nargs="?" — один или ноль параметров
# nargs="*" - ноль или больше параметров
# nargs="+" -  один или больше параметров
# nargs=-1 - хотя бы один параметр, но не ограничен количеством
# nargs=1 - ровно один параметр
# nargs=2 - ровно два параметра и т.д.
