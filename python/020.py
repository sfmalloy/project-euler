# Factorial digit sum
# Project Euler - Problem 20
# Sean Malloy
from functools import reduce
print(sum(map(int, map(str, str(reduce(lambda p, d: p * d, [i for i in
	range(1,101)]))))))
