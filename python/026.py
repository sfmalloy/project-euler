# Reciprocal cycles
# Project Euler - Problem 26
# Sean Malloy
from decimal import Decimal, getcontext

getcontext().prec = 100000

def find_cycles(n):
	frac = str(Decimal(1) / Decimal(n))[2:]
	return frac.count(frac[:50])

upper = 1000
is_prime = [True for i in range(upper + 1)]
is_prime[0] = is_prime[1] = False

for i in range(2, upper+1):
  index = step = i
  if is_prime[index]:
    index += step
    while index <= upper:
      is_prime[index] = False
      index += step

longest = 1000000
longest_i = 0
for i in range(7,1000):
	if is_prime[i]:
		c = find_cycles(i)
		if c < longest:
			longest = c
			longest_i = i
			print('bruh')

print(longest_i)
