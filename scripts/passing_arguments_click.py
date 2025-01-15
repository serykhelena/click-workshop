import logging

import click

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()

# Различия между click.argument и click.option:
# - click.argument используется для обязательных позиционных аргументов, которые передаются без указания флага  # noqa: E501
# - click.option используется для опций, которые передаются c флагами (--или -).


@click.command(help="Пример использования click.argument и click.option")
@click.argument("name", type=str)
# 'name' - обязательный аргумент. Пользователь должен указать без флагов
@click.option("--age", default=18, help="Возраст пользователя (по умолчанию: 18)", type=int)
# '--age' - необязательная опция. Пользователь может указать возраст, используя --age 25 или --age=25  # noqa: E501
@click.option("--debug", is_flag=True, help="Включить режим отладки")
# '--debug' - флаговая опция, которая активируется, если пользователь явно её указывает.
def hello_click(name, age, debug):
    """
    Функция приветствия, использующая Click.
    Аргументы:
    - name (str): Имя пользователя (обязательный позиционный аргумент).
    - age (int): Возраст пользователя (необязательная опция, по умолчанию 18).
    - debug (bool): Флаг режима отладки (по умолчанию False).
    """
    logger.info(f"Привет, {name}!")
    logger.info(f"Возраст {age} лет.")
    if debug:
        logger.info("Режим отладки включен.")


if __name__ == "__main__":
    hello_click()

# Примеры вызова из командной строки:
# python passing_arguments_click.py John
# python script_name.py John --age 25
# python script_name.py John --debug
# python script_name.py John --age 30 --debug
# python script_name.py John --debug --age 30
# python script_name.py --help
# Ошибочные вызовы:
# python script_name.py
# python script_name.py John --age twenty
# python script_name.py John --unknown
