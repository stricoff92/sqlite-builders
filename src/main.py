
import sys

from builders.build_animal_hospital import build as build_animal_hospital
from logger import spawn_logger


if __name__ == "__main__":
    db_name = sys.argv[1]
    logger = spawn_logger()

    if db_name == "animal_hospital":
        build_animal_hospital(logger)
    else:
        raise Exception(f"unknown database name {db_name}")
