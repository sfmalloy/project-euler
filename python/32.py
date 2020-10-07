from itertools import permutations

found = set()
s = 0
for perm in permutations('123456789', 9):
	n = ''.join(perm)
	prod = int(n[5:])
	
	if prod not in found:
		if int(n[0]) * int(n[1:5]) == prod:
			s += prod
			found.add(prod)
		if int(n[0:2]) * int(n[2:5]) == prod:
			s += prod
			found.add(prod)
print(s)

