from ezmaths.coprime import coprime

def test_default():
    assert coprime(8, 10) == False

def test_ints():
    assert coprime(7, 16) == True

def test_random():
    assert coprime(92)