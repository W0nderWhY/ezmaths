from ezmaths import divs, isprime

def factorise(num:int) -> list:
    """Get all prime dividers of integer
    Args:
        num: integer
    Returns:
        List of all prime factors sorted in ascending order.
    """
    factors = []
    while num != 1:
        for i in divs(num):
            if isprime(i):
                factors.append(i)
                num //= i
                break
    return factors