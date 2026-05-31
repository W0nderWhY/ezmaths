import ezmaths

def isprime(num: int) -> bool:
    """Checks if positive number is prime
    Args:
        num: Integer
    Returns:
        Returns bool. True if number is prime, else False
    """
    if num == 1:
        return False
    p = 2
    while p * p <= num:
        if num % p == 0:
            return False
        else:
            p += 1
    return True