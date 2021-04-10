# Pandigital muiltiples
# Project Euler - Problem 38
# Sean Malloy
from itertools import permutations

perms = set(permutations('987654321', 9))
def concat_prod(n):
	prod = ''
	i = 1
	while len(prod) < 9:
		prod += str(n * i)
		i += 1
	if tuple(map(str, prod)) in perms:
		return prod
	return -1

n = 9876
while not concat_prod(n) != -1:
	n -= 1

print(concat_prod(n))
