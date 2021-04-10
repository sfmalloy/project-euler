# Digit factorials
# Project Euler - Problem 34 
# Sean Malloy
def memoize(func):
	memo = {}
	def helper(n):
		if n not in memo:
			memo[n] = func(n)
		return memo[n]
	return helper

@memoize
def fact(n):
	if n == 0:
		return 1
	return n * fact(n - 1)

n = 10
s = 0
while True:
	if sum(map(lambda a: fact(a), map(int, map(str, str(n))))) == n:
		s += n
	if n == 40585:
		break
	n += 1

print(s)
