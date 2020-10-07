from math import sqrt, ceil
def f(n):
	return 4*(n**2) + n + 1

side_length = 1001
print(1 + 4*sum(f(n) for n in range(1, int(0.5*side_length + 0.5))))
