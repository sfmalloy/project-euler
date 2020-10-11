# Convergents of e
# Project Euler - Problem 65
# Sean Malloy
from decimal import Decimal
from fractions import Fraction

stop = 100
terms = []
k = 1
while len(terms) < stop:
	terms.append(1)
	terms.append(2 * k)
	terms.append(1)
	k += 1

def cont_frac(limit, k=0):
	if k == limit - 1:
		return 0
	return Fraction(1, terms[k] + cont_frac(limit, k + 1))

print(sum(map(int, map(str, str((2 + cont_frac(stop)).numerator)))))
