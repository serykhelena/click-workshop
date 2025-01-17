import argparse
import logging
import sys

from colorama import Fore, Style

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        """Кастомный метод error c цветным выводом."""
        sys.stderr.write(f"{Fore.RED}ОШИБКА: {message}{Style.RESET_ALL}\n")
        sys.stderr.write(f"{Fore.YELLOW}Используйте --help для справки.{Style.RESET_ALL}\n")
        self.exit(2)


def main() -> None:
    parser = CustomArgumentParser(description="Пример кастомизации ошибок c цветным выводом")

    parser.add_argument("name", type=str, help="Имя пользователя")

    try:
        args = parser.parse_args()
        logger.info(f"Имя: {args.name}")
    except SystemExit:
        sys.stderr.write(f"{Fore.BLUE}Программа завершена c ошибкой.{Style.RESET_ALL}\n")
        raise


if __name__ == "__main__":
    main()

# Примеры вызова из командной строки:
# python errors_argparce.py

# Нюансы:
# Только переопределение системного вывода
