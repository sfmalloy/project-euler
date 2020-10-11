from math import sqrt
from functools import lru_cache

@lru_cache(maxsize=None)
def ratio(n, factor=2):
	if n > 1:
		prod = 1
		factor = 2
		if n % factor == 0:
			prod *= 1 - (1 / factor)
		while n % factor == 0:
			n /= factor
		factor += 1 if factor == 2 else 2
		return (1 / prod) * ratio(n)
	return 1

limit = 1000000
max_r = 0
max_n = 0
for n in range(limit, 0, -2):
	r = ratio(n)
	if r > max_r:
		max_r = r
		max_n = n
		if max_n != limit:
			break

print(max_n)
