from ezmaths.bin_search import bin_search

def test_default():
    assert bin_search([1, 2, 3, 5, 8], 5, True) == 3

def test_unsorted():
    assert bin_search([1, 5, 3], 5) == 2