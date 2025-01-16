import click


class CustomException(click.ClickException):
    def __init__(self, message):
        super().__init__(message)
        self.exit_code = 1

    def show(self, file=None):
        if file is None:
            file = click.get_text_stream("stderr")
        click.echo(f"Произошла ошибка: {self.message}", fg="red", bold=True, file=file)


@click.command()
@click.argument("word")
def print_word(word):
    """Простейший обработчик, который выводит слово."""
    if not word.isalpha():
        msg = "Слово должно состоять только из букв!"
        raise CustomException(msg)
    click.echo(f"Введенное слово: {word}")


if __name__ == "__main__":
    print_word()

# Примеры вызова:
# python errors_click_4.py hello123

# Нюансы:
#   Для создания кастомных исключений наследуемся от click.ClickException
