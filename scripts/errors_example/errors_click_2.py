import click


class CustomException(click.ClickException):
    def __init__(self, message):
        super().__init__(message)
        self.exit_code = 1

    def format_message(self):
        return f"Произошла ошибка: {self.message}"


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
# python errors_click_2.py hello123

# Нюансы:
#   Для создания кастомных исключений наследуемся от click.ClickException
