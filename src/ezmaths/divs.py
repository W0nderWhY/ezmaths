from typing import Optional

def divs(num: int, include_borders: Optional[bool] = True) -> list[int]:
    """Gets all divisors of a number.

    Args:
        num: Integer whose divisors this function calculates.
        include_borders: Optional bool. If True or None, the result includes 1 
            and the number itself. If False, excludes them. Defaults to True.

    Returns:
        List of integers that are divisors of the given number.
    """
    if include_borders or include_borders == None:
        divisors = [i for i in range(1, num // 2 + 1) if num % i == 0]
        divisors.append(num)
    else:
        divisors = [i for i in range(2, num // 2 + 1) if num % i == 0]
    return divisors