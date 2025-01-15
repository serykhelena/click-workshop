import argparse
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()


def hello_argparse() -> None:
    parser = argparse.ArgumentParser(description="Example of argparse usage")
    parser.add_argument("--name", type=str, help="User's name", required=True)
    parser.add_argument("--age", type=int, help="User's age", required=False, default=18)
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    # Working with arguments
    logger.info(f"Hello, {args.name}!")
    logger.info(f"You are {args.age} years old.")
    if args.debug:
        logger.info("Debug mode enabled.")


if __name__ == "__main__":
    hello_argparse()
