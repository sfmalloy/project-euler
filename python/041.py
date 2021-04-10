# Pandigital prime
# Project Euler - Problem 41
# Sean Malloy
from itertools import permutations
from math import sqrt

def is_prime(p):
	if p <= 1:
		return False
	for i in range(2, int(sqrt(p)) + 1):
		if p % i == 0:
			return False
	return True

perms = []
s = '987654321'
while len(s) > 1:
	perms += [int(''.join(p)) for p in permutations(s)]
	s = s[1:]

i = 0
while i < len(perms) and not is_prime(perms[i]):
	i += 1

print(perms[i])
