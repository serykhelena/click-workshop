from contextlib import contextmanager

import click


@contextmanager
def handle_errors():
    try:
        yield
    except ValueError as error:
        click.echo(f"Произошла ошибка: {error}", err=True)
        raise click.ClickException(str(error)) from error


@click.command()
@click.argument("word")
def print_word(word):
    """Простейший обработчик, который выводит слово."""
    with handle_errors():
        if not word.isalpha():
            msg = "Слово должно состоять только из букв!"
            raise ValueError(msg)
        click.echo(f"Введенное слово: {word}")


if __name__ == "__main__":
    print_word()

# Примеры вызова:
# python errors_click_3.py hello123

# Нюансы:
# B этом примере мы создаем контекстный менеджер handle_errors, который перехватывает исключения ValueError и выводит сообщение
#   ошибки c помощью Click. Затем мы используем этот контекстный менеджер внутри команды print_word.
