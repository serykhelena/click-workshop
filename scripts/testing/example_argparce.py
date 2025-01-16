import argparse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def main():
    parser = argparse.ArgumentParser(description="Сложение двух целых чисел.")
    parser.add_argument("a", type=int, help="Первое целое число")
    parser.add_argument("b", type=int, help="Второе целое число")
    args = parser.parse_args()

    result = args.a + args.b
    logger.info(f"Сумма: {result}")


if __name__ == "__main__":
    main()
