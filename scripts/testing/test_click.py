import unittest

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


# Тесты
class TestAddCommand(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_add_positive_numbers(self):
        result = self.runner.invoke(add, ["3", "5"])
        assert result.exit_code == 0  # noqa: S101
        assert "Сумма: 8" in result.output  # noqa: S101

    def test_invalid_arguments(self):
        result = self.runner.invoke(add, ["three", "5"])
        assert result.exit_code != 0  # noqa: S101
        assert "Invalid value" in result.output  # noqa: S101


if __name__ == "__main__":
    unittest.main()

# Запуск тестов
# python -m unittest test_click.py
