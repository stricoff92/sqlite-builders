


import datetime
import random
from typing import Tuple


def now_date_filename_str() -> str:
    return datetime.datetime.now().strftime(
        "%Y-%m-%d_%H:%M:%S"
    )


def get_random_datetime_range(min_days_ct: int, max_days_ct: int) -> Tuple[datetime.date]:
    if min_days_ct >= max_days_ct:
        raise Exception("invalid min_days_ct/max_days_ct")

    days_ct = random.randint(min_days_ct, max_days_ct)
    last_day_in_range_age_days = random.randint(180, 365)
    today = datetime.date.today()
    last_day_in_range = today - datetime.timedelta(days=last_day_in_range_age_days)
    first_day_in_range = last_day_in_range - datetime.timedelta(days=days_ct)
    return (
        first_day_in_range,
        last_day_in_range,
    )
