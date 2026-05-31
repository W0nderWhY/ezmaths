def factorise(num:int) -> list:
    """Get all prime dividers of integer
    Args:
        num: integer
    Returns:
        List of all prime factors sorted in ascending order.
    """
    factors = []
    p = 2
    while num != 1:
        while num % p == 0:
            num //= p
            factors.append(p)
        p += 1
    return factors