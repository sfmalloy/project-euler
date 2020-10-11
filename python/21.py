# Amicable numbers
# Project Euler - Problem 21
# Sean Malloy
from math import sqrt

def d(n):
	s = 0
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			s += i
			if n // i not in [i, n]:
				s += n // i
	return s

amicable = set()
for i in range(1, 10000):
	d_i = d(i)
	if i not in amicable and d_i not in amicable and i != d_i:
		div = d(d_i)
		if i == div:
			amicable.add(i)
			amicable.add(d_i)
print(sum(amicable))
