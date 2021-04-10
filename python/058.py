# Spiral primes
# Project Euler - Problem 58
# Sean Malloy
from math import sqrt

def f1(n):
	return 4*(n**2) - 2*n + 1

def f2(n):
	return 4*(n**2) + 1

def f3(n):
	return 4*(n**2) + 2*n + 1

def is_prime(n):
	if n < 2:
		return 0
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return 0
	return 1

p = 0
t = 1
n = 1
while True:
	p += is_prime(f1(n)) + is_prime(f2(n)) + is_prime(f3(n))
	t += 4
	if p / t < 0.1:
		break
	else:
		n += 1
print(2*n + 1)
