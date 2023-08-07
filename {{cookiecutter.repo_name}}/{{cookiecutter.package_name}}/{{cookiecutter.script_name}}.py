from time import sleep

import fire
from loguru import logger
from tqdm import tqdm


def main():
    fire.Fire({{cookiecutter.script_name}})


def {{cookiecutter.script_name}}(
    len_loop: int = 10,
    sleep_seconds: float = 0.1,
):
    logger.info("Starting loop")

    for _ in tqdm(range(len_loop)):
        sleep(sleep_seconds)

    logger.info("Finished loop")


if __name__ == "__main__":
    main()
