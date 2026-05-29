import ezmaths

def isprime(num: int) -> bool:
    """Checks if number is prime
    Args:
        num: Integer
    Returns:
        Returns bool. True if number is prime, else False
    """
    if len(ezmaths.divs(num)) == 2:
        return True
    else:
        return False