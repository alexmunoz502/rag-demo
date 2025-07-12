import logging
import sys

from src.config import settings


def get_logger(name: str = __name__) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        logger.setLevel(settings.LOG_LEVEL)

        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
