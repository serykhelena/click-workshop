import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument("word")
def printing(word: str) -> None:
    """Простейший обработчик, который выводит слово."""
    if not word.isalpha():
        msg = "Только буквы!"
        raise ValueError(msg)
    click.echo(f"Введенное слово: {word}")


@cli.result_callback()
def handle_error(result: int) -> int:
    """Обработчик ошибок для команды."""
    try:
        return result
    except ValueError as error:
        click.echo(f"Произошла ошибка: {error}", err=True)
        return 1  # Возвращаем код ошибки


if __name__ == "__main__":
    cli()

# Примеры вызова:
# python errors_click_1.py printing 123

# Нюансы:
#   Для обработки ошибок на уровне группы используется декоратор @group.result_callback на уровне группы
