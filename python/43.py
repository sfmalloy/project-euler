# Sub-string divisibility
# Project Euler - Problem 43 
# Sean Malloy
from itertools import permutations

def special(p):
	divs = [2,3,5,7,11,13,17]
	for i in range(1, 8):
		if int(p[i:i+3]) % divs[i-1] != 0:
			return False
	return True

perms = [''.join(p) for p in permutations('1234567890')]
s = 0
for p in perms:
	s += int(p) if special(p) else 0
print(s)
