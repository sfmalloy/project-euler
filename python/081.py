# Path sum: two ways
# Project Euler - Problem 81
# Sean Malloy
rows = cols = 80

with open('081.txt', 'r') as readfile:
	matrix = []
	for r in readfile.readlines():
		row = list(map(int, r.split(',')))
		matrix.append(row)

def memoize(f):
	memo = {}
	def helper(r, c):
		if (r, c) not in memo:
			memo[(r, c)] = f(r, c)
		return memo[(r, c)]
	return helper

@memoize
def get_sum(r, c):
	if r == rows - 1 and c == cols - 1:
		return matrix[r][c]
	elif r == rows - 1:
		return matrix[r][c] + get_sum(r, c + 1)
	elif c == cols - 1:
		return matrix[r][c] + get_sum(r + 1, c)
	return matrix[r][c] + min(get_sum(r + 1, c), get_sum(r, c + 1))

print(get_sum(0, 0))
