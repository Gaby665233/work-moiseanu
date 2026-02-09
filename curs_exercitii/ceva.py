import sys
print(sys.path)

from math import *
print(pi)  # Uses pi from the math module
print(sqrt(16))


from math import pi, sqrt
print(pi)  # Uses only pi from the math module
print(sqrt(16))


import math
pi = 3.14  # Local variable
print(pi)  # Local value
print(math.pi)  