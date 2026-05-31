from ezmaths import gcd

def coprime(a:int, b:int) -> bool:
    """Checks if two positive integers are coprime (GCD = 1)
    Args:
        a: integer
        b: integer
    Returns:
        bool, True if a and b are coprime, otherwise False
    """
    if gcd(a, b) == 1:
        return True
    else:
        return False