# 10001st prime 
# Project Euler - Problem 7 
# Sean Malloy
from math import sqrt

def is_prime(n):
	limit = int(sqrt(n))
	for i in range(2, limit+1):
		if n % i == 0:
			return False
	return True

count = 1
curr = 3
N = 10001
while count < N:
	count += 1 if is_prime(curr) else 0
	curr += 2

print(curr - 2)
