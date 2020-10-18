# Summation of primes
# Project Euler - Problem 10
# Sean Malloy
from math import sqrt
upper = 2000000
is_prime = [True for i in range(upper + 1)]
is_prime[0] = is_prime[1] = False

i = 2
while i * i <= upper:
	if is_prime[i]:
		index = i * i
		while index <= upper:
			is_prime[index] = False
			index += i
	if i != 2:
		i += 2
	else:
		i = 3

s = 0
for i in range(2, upper+1):
	if is_prime[i]:
		s += i

print(s)
