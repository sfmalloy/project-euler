# Quadratic primes
# Project Euler - Problem 27
# Sean Malloy
from math import sqrt

def memoize(func):
	memo = {}
	def helper(n):
		if n not in memo:
			memo[n] = func(n)
		return memo[n]
	return helper

@memoize
def is_prime(n):
	if n < 0:
		return False
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

def check_quad(a, b):
	n = 0
	count = 0
	while (is_prime(n**2 + a*n + b)):
		count += 1
		n += 1
	return count

max_num_primes = 0
max_prod = 0
for a in range(-997, 998):
	for b in range(-997, 998):
		prime_count = check_quad(a, b)
		if max_num_primes < prime_count:
			max_num_primes = prime_count
			max_prod = a * b

print(max_prod)
