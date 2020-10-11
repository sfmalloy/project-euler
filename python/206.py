# Concealed Square
# Project Euler - Problem 206
# Sean Malloy

from math import sqrt

digits = []
for i in range(1, 10):
	digits.append(i)
	digits.append(0)
digits.append(0)

def concat(digits):
	num = 0
	pow10 = 1
	for i in range(len(digits) - 1, -1, -1):
		num += pow10 * digits[i]
		pow10 *= 10
	return num

n = 1235100000
print(len(str(n**2)))
while len(str(n**2)) == 19:
	print(n, n**2)
	n += 1
