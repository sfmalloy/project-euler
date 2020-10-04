a = b = 1
s = 0
while a <= 4000000:
	s += a if a % 2 == 0 else 0
	t = a
	a = b
	b += t
print(s)
