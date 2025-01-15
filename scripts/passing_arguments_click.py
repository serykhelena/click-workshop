import logging

import click

# settings
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()


@click.command(help="Example of using click")
@click.argument("name", type=str)
@click.option("--age", default=18, help="User's age", type=int)
@click.option("--debug", is_flag=True, help="Enable debug mode")
def hello_click(name, age, debug) -> None:
    # Working with arguments
    logger.info(f"Hello, {name}!")
    logger.info(f"You are {age} years old.")
    if debug:
        logger.info("Debug mode enabled.")


if __name__ == "__main__":
    hello_click()
