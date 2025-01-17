import click
from click_help_colors import HelpColorsCommand, HelpColorsGroup


@click.group(
    cls=HelpColorsGroup,
    help_headers_color="yellow",  # Цвет заголовков справки
    help_options_color="green",  # Цвет опций
)
def cli():
    """Основная команда CLI."""


@cli.command(
    cls=HelpColorsCommand,
    help_headers_color="cyan",  # Цвет заголовков справки команды
    help_options_color="blue",  # Цвет опций команды
    help="Демонстрация цветной справки",
)
def display_text():
    """Демонстрация изменения текста c помощью Click."""
    # Обычный текст
    click.secho("Обычный текст")

    # Цветной текст
    click.secho("Это текст красного цвета", fg="red")
    click.secho("Это текст зеленого цвета", fg="green")

    # Цветной текст c измененным фоном
    click.secho("Текст c синим фоном", bg="blue", fg="white")

    # Жирный текст
    click.secho("Это жирный текст", bold=True)

    # Подчеркнутый текст (в некоторых терминалах может не работать)
    click.secho("Это подчеркнутый текст", underline=True)

    # Комбинация стилей
    click.secho("Жирный, белый текст на красном фоне", fg="white", bg="red", bold=True)


if __name__ == "__main__":
    display_text()

# Примеры вызова:
# python terminal_click.py
# python terminal_click.py display_text --help

# Нюансы:
#   Для изменения цвета текста используется click.secho c модификаторами
#   Для изменения цвета текста в справке используется HelpColorsCommand в click.group и click.command
