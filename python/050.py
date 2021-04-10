# Consecutive prime sum
# Project Euler - Problem 50
# Sean Malloy
from math import sqrt

limit = 10**6

primes = [True for _ in range(limit)]
primes[0] = primes[1] = False

s = 0
largest_add = 0
for p in range(2, len(primes)):
	if primes[p]:
		index = 2 * p
		while index < len(primes):
			primes[index] = False
			index += p
		if s < limit:
			s += p
			largest_add = p
			print(s, largest_add)

s -= largest_add
p = 2

while not primes[s]:
	s -= p
	p += 1 if p == 2 else 2
print(s)
