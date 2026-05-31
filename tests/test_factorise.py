from ezmaths.factorise import factorise

def test_default():
    assert factorise(50) == [2, 5, 5]

def test_prime():
    assert factorise(7) == [7]

def test_ints():
    assert factorise(15) == [3, 5]

def test_eight():
    assert factorise(8) == [2, 2, 2]

def test_24():
    assert factorise(24) == [2, 2, 2, 3]