# Lexicographic permutations
# Project Euler - Problem 24
# Sean Malloy
from itertools import permutations
print(''.join(list(permutations('0123456789', 10))[999999]))
