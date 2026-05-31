from ezmaths.factorise import factorise

def test_default():
    assert factorise(20) == [2, 5, 5]

def test_prime():
    assert factorise(7) == [7]

def test_ints():
    assert factorise(15) == [3, 5]