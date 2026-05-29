from ezmaths.isprime import isprime

def test_isprime_default():
    assert isprime(12) == False

def test_isprime_prime():
    assert isprime(7) == True

def test_isprime_one():
    assert isprime(1) == False