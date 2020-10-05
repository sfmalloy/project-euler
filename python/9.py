def get_n(m):
	return (500 - m**2) / m

m = 2
while m < get_n(m) and get_n(m) != 0:
	print(m, get_n(m))
	m += 1
print(m, get_n(m))
