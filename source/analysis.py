from typing import List
from exceptions import NegativeValueError


def average(values: List[int | float]) -> int:
    total: int = 0
    try:
        for value in values:
            if value >= 0:
                total += value
            else: raise NegativeValueError(value)

    except NegativeValueError as error:
        raise error

    return round(total / len(values))