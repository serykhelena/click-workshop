import logging

import click

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@click.command()
@click.option(
    "--flag",
    is_flag=True,  # Флаг, который устанавливает значение True
    help="Включить флаг",
)
def main(flag):
    """Пример работы c флагами в click."""
    if flag:
        click.echo("Включен флаг")
    else:
        click.echo("Флаг не включен")


if __name__ == "__main__":
    main()

# Примеры вызова из командной строки:
# python flag_click.py --flag
# python flag_click.py

# Нюансы:
# Для определения флага используется опция is_flag=True, что позволяет флагу устанавливать значение True
# Для флагов значение по умолчанию также False, но можно изменить, явно указав параметр default
