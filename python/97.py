# Large non-Mersenne prime
# Project Euler - Problem 97
# Sean Malloy

def d(i):
	return (2 * i) % 10000000000

p = 2
for i in range(2, 7830457 + 1):
	p = d(p)

print((28433*p + 1) % 10000000000)
