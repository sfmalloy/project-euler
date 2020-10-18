# Prime permutations
# Project Euler - Problem 49
# Sean Malloy
from itertools import permutations
from functools import reduce
from math import sqrt

def concat(a, b):
	return a + b

limit = 9999
prime = [True for i in range(limit + 1)]
prime[0] = prime[1] = False

prime_limit = int(sqrt(limit))
for p in range(2, prime_limit + 1):
	if prime[p]:
		index = p * p
		while index <= limit:
			prime[index] = False
			index += p

for p in range(1489, limit + 1, 2):
	if prime[p]:
		perms = list(map(lambda x: int(reduce(lambda a, b: a + b, x)),
			permutations(str(p))))
		prime_perms = [p]
		for perm in perms:
			if perm - prime_perms[-1] == 3330 and prime[perm]:
				prime_perms.append(perm)
		if len(prime_perms) == 3:
			[print(perm, end='') for perm in prime_perms]
			break
print('')
