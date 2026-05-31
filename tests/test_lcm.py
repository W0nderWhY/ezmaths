from ezmaths.lcm import lcm

def test_default():
    assert lcm(3, 2) == 6

def test_coprime():
    assert lcm(7, 4) == 28

def test_ints():
    assert lcm(8, 24) == 24