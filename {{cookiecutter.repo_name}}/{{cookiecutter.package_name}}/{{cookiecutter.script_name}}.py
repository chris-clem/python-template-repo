from time import sleep

from loguru import logger
from tqdm import tqdm


def main(len_loop: int = 10, sleep_secs: int = 1):
    logger.info(f"{len_loop=}, {sleep_secs=}")

    for _ in tqdm(range(len_loop)):
        sleep(sleep_secs)


if __name__ == "__main__":
    main()
