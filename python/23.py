# Non-abundant sums
# Project Euler - Problem 23
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

abundant = []
for i in range(1, 28123):
	if d(i) > i:
		abundant.append(i)

sums = set()
for i in range(len(abundant)):
	for j in range(i, len(abundant)):
		sums.add(abundant[i] + abundant[j])

s = 0
for i in range(1, 28124):
	if i not in sums:
		s += i

print(s)
