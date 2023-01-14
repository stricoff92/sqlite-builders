
import logging
import sys

def spawn_logger() -> logging.Logger:
    logger = logging.getLogger("sqlite-builders")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.debug("logger created")
    return logger
