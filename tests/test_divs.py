from ezmaths.divs import divs

def test_divs_default():
    assert divs(12) == [1, 2, 3, 4, 6, 12]

def test_divs_without_borders():
    assert divs(12, include_borders=False) == [2, 3, 4, 6]

def test_divs_prime_number():
    assert divs(7) == [1, 7]

def test_divs_negative():
    assert divs(-6) == [-6, -3, -2, -1, 1, 2, 3, 6]