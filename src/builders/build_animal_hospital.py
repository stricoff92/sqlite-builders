
from logging import Logger
import sqlite3

from utils.file_names import get_out_file_name
from utils.datetime import get_random_datetime_range


def _build(
    logger: Logger,
    con: sqlite3.Connection,
    out_file_name: str,
    out_full_path: str,
):
    (
        range_start,
        range_end,
    ) = get_random_datetime_range(600, 1000)
    logger.debug(f"out_file_name '{out_file_name}'")
    logger.debug(f"out_full_path '{out_full_path}'")
    logger.debug(f"range_start '{range_start.strftime('%b %d, %Y')}'")
    logger.debug(f"range_end '{range_end.strftime('%b %d, %Y')}'")

    cur = con.cursor()

    # create database tables using DDL
    cur.execute('''
        CREATE TABLE "customer" (
        "id"	        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "first_name"    TEXT NOT NULL,
        "last_name"	    TEXT NOT NULL,
        "email"	        TEXT NOT NULL
    );
    ''')
    con.commit()
    cur.execute('''
        CREATE TABLE "service" (
        "id"	  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "name"    TEXT NOT NULL
    );
    ''')
    con.commit()
    cur.execute('''
        CREATE TABLE "species_type" (
        "id"	  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "name"    TEXT NOT NULL
    );
    ''')
    con.commit()
    cur.execute('''
        CREATE TABLE "species" (
        "id"	  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "name"    TEXT NOT NULL,
        "species_type_id" INTEGER NOT NULL,
        FOREIGN KEY(species_type_id) REFERENCES species_type(id)
    );
    ''')
    con.commit()
    cur.execute('''
        CREATE TABLE "animal" (
        "id"	  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "name"    TEXT NOT NULL,
        "species_id" INTEGER NOT NULL,
        "customer_id" INTEGER NOT NULL,
        FOREIGN KEY(species_id) REFERENCES species(id),
        FOREIGN KEY(customer_id) REFERENCES customer(id)
    );
    ''')
    con.commit()
    cur.execute('''
        CREATE TABLE "invoice" (
        "id"	  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "customer_id" INTEGER NOT NULL,
        "created_at"    TEXT NOT NULL,
        "due_at"    TEXT NOT NULL,
        FOREIGN KEY(customer_id) REFERENCES customer(id)
    );
    ''')
    con.commit()
    cur.execute('''
        CREATE TABLE "invoice_row" (
        "id"	        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "invoice_id"    INTEGER NOT NULL,
        "animal_id"     INTEGER NOT NULL,
        "service_id"    INTEGER NOT NULL,
        "cost_cents"    INTEGER NOT NULL,
        FOREIGN KEY(invoice_id) REFERENCES invoice(id)
        FOREIGN KEY(animal_id) REFERENCES animal(id)
        FOREIGN KEY(service_id) REFERENCES service(id)
    );
    ''')
    con.commit()
    cur.execute('''
        CREATE TABLE "payment" (
        "id"	        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "invoice_id"    INTEGER NOT NULL,
        "cost_cents"    INTEGER NOT NULL,
        FOREIGN KEY(invoice_id) REFERENCES invoice(id)
    );
    ''')
    con.commit()


    # Populate Services
    cur.execute('''
        INSERT INTO service (id, name)
        VALUES
            (1, "Spaying"),
            (2, "Neutering"),
            (3, "Deworming"),
            (4, "General Anesthesia"),
            (5, "Local Anesthesia"),
            (6, "IV Fluids"),
            (7, "Rabies Shot"),
            (8, "Claw Clipping"),
            (9, "Broken Bone Setting"),
            (10, "Bloodwork"),
            (11, "Teeth Cleaning"),
            (12, "X-Ray");
    ''')
    con.commit()

    # Populate species type
    cur.execute('''
        INSERT INTO species_type (id, name)
        VALUES
            (1, "Mammal Medium"),
            (2, "Mammal Large"),
            (3, "Mammal Small"),
            (4, "Reptile/Amphibian"),
            (5, "Bird");
    ''')
    con.commit()

    # Populate species
    cur.execute('''
        INSERT INTO species (id, species_type_id, name)
        VALUES
            (1, 1, "Cat"),
            (2, 1, "Dog"),
            (3, 1, "Rabbit"),
            (4, 1, "Pig"),
            (5, 2, "Dog 100LBs+"),
            (6, 2, "Pig 100LBs+"),
            (7, 2, "Horse"),
            (8, 2, "Cow"),
            (9, 2, "Goat/Donkey/Mule"),
            (10, 3, "Gerbil"),
            (11, 3, "Guinea Pig"),
            (12, 3, "Rat"),
            (13, 3, "Mouse"),
            (14, 4, "Gecko"),
            (15, 4, "Snake"),
            (16, 4, "Turtle"),
            (17, 4, "Frog/Toad"),
            (18, 4, "Monitor Lizard"),
            (19, 4, "Bearded Dragon"),
            (20, 5, "Parakeet"),
            (21, 5, "Parrot"),
            (22, 5, "Cockatiel");
    ''')
    con.commit()


def build(logger: Logger):
    (
        out_file_name,
        out_full_path,
    ) = get_out_file_name("animal_hospital")
    logger.info("opening database connection")
    con = sqlite3.connect(out_full_path)
    try:
        _build(logger, con, out_file_name, out_full_path)
    except Exception:
        raise
    finally:
        logger.info("closing database connection")
        con.close()
