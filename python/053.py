# Combinatoric selections
# Project Euler - Problem 53
# Sean Malloy

from functools import lru_cache

@lru_cache(maxsize=None)
def fact(n):
	if n < 2:
		return 1
	return n * fact(n - 1)

def comb(n, r):
	return fact(n) // (fact(r) * fact(n - r))

count = 0
for n in range(1, 101):
	for r in range(0, n + 1):
		count += 1 if comb(n, r) > 1000000 else 0

print(count)
