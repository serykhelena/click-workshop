import argparse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def main() -> None:
    parser = argparse.ArgumentParser(description="Пример обязательного позиционного аргумента")

    # Добавляем обязательный позиционный аргумент
    parser.add_argument("name", type=str, help="Имя пользователя")
    # Добавляем обязательную опцию
    parser.add_argument("--email", type=str, required=True, help="Email пользователя")
    # Добавляем необязательную опцию
    parser.add_argument("--age", type=int, help="Возраст пользователя")
    # Добавляем необязательную опцию, которая может принимать максимум 1 значение
    parser.add_argument("--id_user", type=int, nargs="?", help="id пользователя")

    args = parser.parse_args()

    logger.info(f"Ваш email: {args.email}")

    logger.info(f"Привет, {args.name}!")

    if args.age:
        logger.info(f"Ваш возраст: {args.age}")
    if args.id_user:
        logger.info(f"Ваш id: {args.id_user}")


if __name__ == "__main__":
    main()

# Примеры вызова из командной строки:
# python needed_argument_argparce.py John --email=@abc.com
# python needed_argument_argparce.py John --email=@abc.com --age 30
# python needed_argument_argparce.py John --email=@abc.com --age 30 --id_user 101
# python needed_argument_argparce.py John --email=@abc.com --id_user 101

# Нюансы:
# Позиционные аргументы всегда обязательны
# Опции обязательны только при наличии аргумента required=True
#   required применяется только к опциям
# Опции, помеченные как nargs="?", могут принимать одно значение или вообще не принимать
