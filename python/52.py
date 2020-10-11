# Permuted Multiples
# Project Euler - Problem 52
# Sean Malloy
from functools import reduce

def concat(a, b):
	return a + b

def sort_int(n):
	return int(reduce(concat, sorted(str(n))))

x = 1
while True:
	test = sort_int(x)
	found = True
	for i in range(2, 6):
		if sort_int(i * x) != test:
			found = False
			break
	
	if found:
		break
	x += 1

print(x)
