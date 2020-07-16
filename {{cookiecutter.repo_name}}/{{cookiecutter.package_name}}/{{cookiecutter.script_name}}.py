from pprint import pformat
from time import sleep

import click
from loguru import logger
from tqdm import tqdm


@click.command()
@click.option(
    "-l",
    "--len_loop",
    default=100,
    type=click.INT,
    show_default=True,
    help="Length of the tqdm loop",
)
@click.option(
    "-s",
    "--sleep_seconds",
    default=0.01,
    type=click.FLOAT,
    show_default=True,
    help="Amount of seconds to sleep",
)
def main(**kwargs):
    logger.info(f"kwargs:\n{pformat(kwargs)}")

    for _ in tqdm(range(kwargs["len_loop"])):
        sleep(kwargs["sleep_seconds"])


if __name__ == "__main__":
    main()
