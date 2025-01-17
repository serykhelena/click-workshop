import logging

import click

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@click.group()
def cli():
    """
    Основная группа команд.
    """


def lazy_add(a: int, b: int) -> int:
    """
    Ленивая композиция аргументов для сложения.
    Сложение выполняется только при вызове функции.
    """

    def add() -> int:
        result = a + b
        logger.info("Непосредственное выполнение сложения")
        logger.info(f"Результат сложения: {result}")

    return add


@click.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
def add(a: int, b: int) -> None:
    """
    Команда для сложения двух чисел c ленивой композицией.
    """
    # Создание функции сложения, которая будет вызвана только при необходимости
    add_function = lazy_add(a, b)
    logger.info("Функция сложения создана, но не вызвана.")
    # Вызываем результат сложения
    logger.info("Вызываем функцию сложения.")
    add_function()
    logger.info("Функция сложения вызвана.")


# Добавляем команды в группу
cli.add_command(add)

if __name__ == "__main__":
    cli()

# Пример использования:
# python lazy_click.py add 10 20
