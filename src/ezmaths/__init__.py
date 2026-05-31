"""
**Ezmaths** *is library to optimize routine things in programming. Some features from 0.1.0*:
* *Binary search*
* *Factorise*
* *Dividers of number*
* *GCD and LCM*
"""

from .divs import divs
from .bin_search import bin_search
from .isprime import isprime
from .gcd import gcd
from .lcm import lcm
from .coprime import coprime
from .factorise import factorise

__all__ = [
    "divs",
    "bin_search",
    "isprime",
    "gcd",
    "lcm",
    "coprime",
    "factorise"
]