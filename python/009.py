# Special Pythagorean triplet 
# Project Euler - Problem 9
# Sean Malloy
a = b = c = 0
for m in range(22,0,-1):
	n = (500/m) - m
	if n % 1 == 0:
		a = m**2 - n**2
		b = 2*m*n
		c = m**2 + n**2
		print(int(a*b*c))
		break
