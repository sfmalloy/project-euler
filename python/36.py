# Double-base palindromes
# Project Euler - Problem 36 
# Sean Malloy
def is_pal(n):
	s = str(n).split('b')[-1]
	b = len(s) - 1
	for f in range(len(s) // 2):
		if s[f] != s[b]:
			return False
		b -= 1
	return True

MAX = 1000000
s = 0
for i in range(1, MAX, 2):
	if is_pal(i) and is_pal(bin(i)):
		s += i
print(s)
