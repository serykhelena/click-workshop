import logging
from pathlib import Path

import click

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# ctx: Объект контекста текущей команды.
# param: Объект параметра, который вызывает функцию.
def comma_separated_list(ctx, param, value):  # noqa: ARG001
    """
    Пример пользовательской функции для преобразования строкового аргумента
    в список, разделённый запятыми.
    """
    if value is None:
        return None
    try:
        return value.split(",")
    except Exception:
        msg = f"'{value}' не является корректным списком через запятую"
        raise click.BadParameter(msg) from None


@click.command(help="Расширенный пример типизации c click")
@click.argument("name", type=str)
@click.argument("age", type=int)
@click.option("--pi", type=float, default=3.14, help="Произвольное число c плавающей точкой")
@click.option("--tags", callback=comma_separated_list, help="Список тегов, разделённых запятыми")
@click.option("--optional", type=str, help="Опциональный аргумент без явного типа")
@click.option(
    "--color",
    type=click.Choice(["red", "green", "blue"], case_sensitive=False),
    help="Выбор цвета из предопределённых значений",
)
@click.option(
    "--config",
    type=click.File("r"),
    help="Файл конфигурации для чтения",
)
@click.option(
    "--path",
    type=click.STRING,
    help="Путь к файлу или директории",
)
@click.option(
    "--coordinates",
    type=(float, float),
    multiple=True,
    help="Множественные значения координат (например, --coordinates 1.0 2.0 --coordinates 3.0 4.0)",
)
def main(  # noqa: PLR0913
    name: str,
    age: int,
    pi: float,
    tags: list,
    optional: str,
    color: str,
    config: click.File,
    path: str,
    coordinates: list[tuple[float, float]],
):
    logger.info(f"Имя: {name} (тип: {type(name)})")
    logger.info(f"Возраст: {age} (тип: {type(age)})")
    logger.info(f"Число π: {pi} (тип: {type(pi)})")

    if tags:
        logger.info(f"Теги: {tags} (тип: {type(tags)})")
    if optional:
        logger.info(f"Значение 'optional': {optional} (тип: {type(optional)})")
    if color:
        logger.info(f"Цвет: {color} (тип: {type(color)})")
    if config:
        logger.info(f"Содержимое файла конфигурации: {config.read()}")
    if path:
        # Преобразование строки в путь
        path = Path(path)
        # Использование пути
        if path.exists():
            logger.info(f"Путь существует: {path} (тип: {type(path)})")
        else:
            logger.warning(f"Путь не существует: {path} (тип: {type(path)})")
    if coordinates:
        logger.info(f"Координаты: {coordinates} (тип: {type(coordinates)})")


if __name__ == "__main__":
    main()

# Примеры вызова из командной строки:
# python typing_argument_click.py John 25
# python typing_argument_click.py John 25 --color red
# python typing_argument_click.py John 25 --config ../configs/config.txt
# python typing_argument_click.py John 25 --path ../configs/
# python typing_argument_click.py John 25 --coordinates 1.0 2.0 --coordinates 3.0 4.0
# Нюансы:
# Click предоставляет собственные классы типов для расширенных сценариев: click.Choice, click.File,
#   click.Path, click.IntRange
# Click позволяет создавать пользовательские функции обработки, которые выступают в роли типов
# Click поддерживает типизацию на уровне аргументов групп команд
