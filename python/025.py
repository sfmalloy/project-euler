# 1000-digit Fibonacci number
# Project Euler - Problem 25
# Sean Malloy
a = b = 1
i = 1
while len(str(b)) != 1000:
	t = a
	a = b
	b += t
	i += 1
print(i + 1)

