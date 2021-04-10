# Champernowne's constant
# Project Euler - Problem 40 
# Sean Malloy
champ = ''
i = 0
while len(champ) <= 1000000:
	champ += str(i)
	i += 1

n = 1
prod = 1
while n <= 1000000:
	prod *= int(champ[n])
	n *= 10
print(prod)
