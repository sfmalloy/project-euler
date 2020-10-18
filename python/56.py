# Powerful digit sum
# Project Euler - Problem 56
# Sean Malloy

def digit_sum(a, b):
	return sum(map(int, map(str, str(a**b))))

m = 0
for a in range(100):
	for b in range(100):
		m = max(digit_sum(a, b), m)

print(m)
