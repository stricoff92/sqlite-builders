
import os.path
from typing import Tuple

from constants import OUT_DIR
from utils.datetime import now_date_filename_str


def get_out_file_name(database_name: str) -> Tuple[str]:
    out_file_name = f'{database_name}_{now_date_filename_str()}.sqlite3'
    out_full_path = os.path.join(OUT_DIR, out_file_name)
    return out_file_name, out_full_path
