# Square digit chains
# Project Euler - Problem 92
# Sean Malloy

def memoize(f):
	memo = {}
	def helper(n):
		if n not in memo:
			memo[n] = f(n)
		return memo[n]
	return helper

def ssd(n):
	return sum(i**2 for i in map(int, map(str, str(n))))

@memoize
def chain(n):
	if n == 89:
		return True
	if n == 1:
		return False
	return chain(ssd(n))

count = 0
for i in range(2, 10**7):
	print(i)
	count += int(chain(i))

print(count)
