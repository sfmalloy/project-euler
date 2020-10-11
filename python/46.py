# Goldbach's other conjecture
# Project Euler - Problem 46
# Sean Malloy
from math import sqrt
from functools import lru_cache

@lru_cache(maxsize=None)
def is_prime(n):
	if n < 2:
		return False
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

n = 9
while True:
	found = False
	if not is_prime(n):
		found = True
		k = 1
		d = n - 2*(k**2)
		while d > 0:
			if is_prime(d):
				print(f'{n} = {d} - 2*{k}^2')
				found = False
				break
			k += 1
			d = n - 2*(k**2)
	if found:
		break
	n += 2

print(n)
