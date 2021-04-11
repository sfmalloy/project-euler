# Largest exponential
# Project Euler - Problem 99
# Sean Malloy
from math import log2

with open('099.txt', 'r') as readfile:
	pairs = [p.rstrip() for p in readfile.readlines()]

max_val = 0
max_line = 0
for p, l in zip(pairs, range(1, len(pairs) + 1)):
	base, exp = map(int, p.split(','))
	val = exp * log2(base)
	if val > max_val:
		max_line = l
		max_val = val

print(max_line)
