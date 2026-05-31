from ezmaths.gcd import gcd

def test_default():
    assert gcd(20, 15) == 5

def test_ints():
    assert gcd(14, 28) == 14

def test_primes():
    assert gcd(7, 52) == 1