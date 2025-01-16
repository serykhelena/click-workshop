import logging

import click

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()

# Различия между click.argument и click.option:
# - click.argument используется для обязательных позиционных аргументов
#       Обязательны. Важен порядок передачи. Определяют минимальный набор параметров
#       Может быть любым базовым или кастомным типом
#       help напрямую указать нельзя
#           (можно указать опосредованно через help описания функции)
# - click.option используется для опций, которые передаются c флагами (--или -)
#       Обязательность задаётся отдельным параметром
#       Неважен порядок передачи
#       Поддерживает значения по умолчанию (default), флаги (is_flag=True), help и другие настройки


@click.command(help="Функция приветствия")
@click.argument("name", type=str)
# 'name' - обязательный аргумент. Пользователь должен указать без флагов
@click.option("--age", default=18, help="Возраст пользователя (по умолчанию: 18)", type=int)
# '--age' - необязательная опция. Пользователь может указать возраст, используя --age 25 или --age=25
@click.option("--id_user", help="Идентификатор пользователя", type=int)
# '--id' - необязательная опция. Пользователь может указать id
@click.option("--debug", is_flag=True, help="Включить режим отладки")
# '--debug' - флаговая опция, которая активируется, если пользователь явно её указывает.
def hello_click(name: str, age: int, id_user: int | None, debug: bool) -> None:  # noqa: FBT001
    """
    Функция приветствия.

    Аргументы:
    - name (str): Имя пользователя (обязательный позиционный аргумент).
    - age (int): Возраст пользователя (опция с указанным значением по умолчанию).
    - id_user (Optional[int]): Идентификатор пользователя (опционально).
    - debug (bool): Флаг включения режима отладки.
    """  # noqa: RUF002
    logger.info(f"Привет, {name}!")
    logger.info(f"Возраст: {age} лет.")

    if id_user is not None:
        logger.info(f"ID пользователя: {id_user}")

    if debug:
        logger.info("Режим отладки включен.")


if __name__ == "__main__":
    hello_click()

# Примеры вызова из командной строки:
# python passing_arguments_click.py John
# python passing_arguments_click.py John --age 25
# python passing_arguments_click.py John --debug
# python passing_arguments_click.py John --age 30 --debug
# python passing_arguments_click.py John --debug --age 30
# python passing_arguments_click.py John --id_user=42
# python passing_arguments_click.py --help
# Ошибочные вызовы:
# python passing_arguments_click.py
# python passing_arguments_click.py John --age twenty
# python passing_arguments_click.py John --unknown
