from itertools import combinations, product
import unittest
import random
import re

# 3 1000
# 2 5 4
# 3 7 8 9
# 5 5 7 8 9 10


string = "100,000,000.000"
result = re.split(r"[,\.]", string)

print(result)