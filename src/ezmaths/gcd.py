def gcd(a:int, b:int) -> int:
    """Get Greatest Common Divider(GCD) of two positive integers
    Args:
        a: integer
        b: integer
    Returns:
        Integer, GCD of a and b
    """
    while b != 0:
        a, b = b, a % b
    return a