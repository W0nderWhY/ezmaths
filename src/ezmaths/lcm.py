from ezmaths import gcd

def lcm(a:int, b:int) -> int:
    """Get Lowest Common Multiple of two integers
    Args:
        a: integer
        b: integer
    Returns:
        Integer, LCM of a and b
    """
    return int((a * b) / gcd(a, b))