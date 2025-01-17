import click
from click.testing import CliRunner


# Приложение Click для сложения двух чисел
@click.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
def add(a: int, b: int) -> None:
    """
    Складывает два числа и выводит результат.
    """
    result = a + b
    click.echo(f"Сумма: {result}")


# Тесты c использованием pytest
def test_add_positive_numbers():
    runner = CliRunner()
    result = runner.invoke(add, ["3", "5"])
    assert result.exit_code == 0
    assert "Сумма: 8" in result.output


def test_invalid_arguments():
    runner = CliRunner()
    result = runner.invoke(add, ["three", "5"])
    assert result.exit_code != 0
    assert "Invalid value" in result.output


# Запуск тестов
# pytest test_click.py

# Нюансы:
# Есть модуль click.testing c раннером CliRunner
# CliRunner сам перехватывает вывод и позволяет проверить exit code.
# Позволяет тестировать click-утилиты без использования pytest и обходиться стандартным модулем unittest
