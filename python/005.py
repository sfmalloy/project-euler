# Smallest multiple
# Project Euler - Problem 5
# Sean Malloy

found = False
n = 20
while not found:
	found = True
	for i in range(1, 21):
		if n % i != 0:
			found = False
			break
	if not found:
		n += 20

print(n)

