# Largest product in a series
# Project Euler - Problem 8
# Sean Malloy
from functools import reduce

LIMIT				= 13
LINE_LENGTH = 50

with open('8.txt', 'r') as readfile:
	lines = [list(map(int, map(str, line.strip()))) for line in readfile.readlines()]
	digits = []
	for line in lines:
		digits += line

prod = 0
for i in range(0, len(digits) - LIMIT + 1):
	if i % LINE_LENGTH == LINE_LENGTH - LIMIT:
		i = LINE_LENGTH
	prod = max(prod, reduce(lambda p, d: p * d, digits[i:i+LIMIT]))

print(prod)
