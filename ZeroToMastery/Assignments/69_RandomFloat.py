"""
Please generate a random float where the value is between 5 and 95 using Python module.

Hints
Use random.random() to generate a random float in [0,1].

"""

import random
rand = round(random.uniform(5, 95), 4)
print(rand)
