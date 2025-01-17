import logging
import sys

import click

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("example_logger")


@click.command(help="Пример использования click.echo, print и logger")
@click.argument("message", type=str)
@click.option("--use-echo", is_flag=True, help="Использовать click.echo для вывода")
@click.option("--use-print", is_flag=True, help="Использовать print для вывода")
@click.option("--use-logger", is_flag=True, help="Использовать logger для вывода")
@click.option("--error", is_flag=True, help="Вывести сообщение в stderr")
@click.option("--styled", is_flag=True, help="Применить стилизацию к сообщению")
def main(  # noqa: PLR0913
    message: str,
    use_echo: bool,
    use_print: bool,
    use_logger: bool,
    error: bool,
    styled: bool,
):
    """
    Демонстрация особенностей вывода в CLI.
    """
    # Вывод через click.echo
    if use_echo:
        output_file = sys.stderr if error else sys.stdout
        styled_message = click.style(message, fg="green", bold=True) if styled else message
        click.echo(styled_message, file=output_file)

    # Вывод через print
    if use_print:
        if error:
            print(f"Ошибка: {message}", file=sys.stderr)  # noqa: T201
        else:
            print(message)  # noqa: T201

    # Логирование через logger
    if use_logger:
        if error:
            logger.error(message)
        else:
            logger.info(message)


if __name__ == "__main__":
    main()

# Примеры вызова из командной строки:
# python echo_click.py "Hello, Click!" --use-echo --styled
# python echo_click.py "Hello, Click!" --use-echo > output.txt
# python echo_click.py "Hello, Print!" --use-print
# python echo_click.py "Hello, Logger!" --use-logger
# python echo_click.py "This is an error!" --use-echo --error
# python echo_click.py "This is an error!" --use-print --error

# Нюансы:
# click.echo: Обеспечивает корректную обработку символов Unicode и автоматически
#   использует правильную кодировку в зависимости от системы
# click.echo: Поддерживает аргумент file, позволяя легко перенаправлять вывод в файл,
#   стандартный поток ошибок (sys.stderr) или любой другой поток.
# click.echo: Используется для сообщений, предназначенных для пользователя,
#   как часть интерфейса приложения
