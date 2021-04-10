# Largest prime factor 
# Project Euler - Problem 3
# Sean Malloy

N = int(input())
factor = 2
while N > 1:
	if N % factor == 0:
		N /= factor
	if N > 1:
		factor += 1 if factor == 2 else 2
print(int(factor))
