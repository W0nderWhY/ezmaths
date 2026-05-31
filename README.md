# ezmaths 📐

Small library to optimize your routine in solving math problems. Includes some basic functions, which developers are sometimes lazy to write by themselves.

## Quick Start 💻

That's how you can use this library to find divisors of number:

```python
from ezmaths import divs

# By default, function returns all divisors of a number including 1 and number itself
print(divs(12)) 
# Output: [1, 2, 3, 4, 6, 12]

# If you need divisors excluding 1 and number itself, use include_borders=False
print(divs(12, include_borders=False)) 
# Output: [2, 3, 4, 6]
```