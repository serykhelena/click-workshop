from enum import Enum

import click


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

    @classmethod
    def values(cls):
        return [color.value for color in cls]


@click.command()
@click.option("--color", type=click.Choice(Color.values()), help="Выберите цвет.")
def choose_color(color):
    click.echo(f"Вы выбрали цвет: {color}")


if __name__ == "__main__":
    choose_color()

# Пример вызова
# python enum_and_choice_click.py --color red

# Нюансы:
# click.Choice на вход ожидает только строки. Поэтому напрямую передать значение
# в виде ссылки из enum невозможно
