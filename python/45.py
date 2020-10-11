# Triangular, pentagonal, and hexagonal
# Project Euler - Problem 45
# Sean Malloy
from math import sqrt

def H(n):
	return n * (2*n - 1)

def find_k(n):
	return (1 + sqrt(24*H(n) + 1)) / 6

n = 144
while find_k(n) % 1 != 0:
	n += 1

print(H(n))
