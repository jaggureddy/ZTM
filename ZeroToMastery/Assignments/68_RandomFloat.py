"""
Please generate a random float where the value is between 10 and 100 using Python module.

Hints
Use random.random() to generate a random float in [0,1].

"""

import random
rand_num = round(random.uniform(10, 100), 4)
print(rand_num)
