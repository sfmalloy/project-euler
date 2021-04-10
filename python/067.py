# Maximum path sum II
# Project Euler - Problem 67
# Sean Malloy
class node:
	def __init__(self, val, left=-1, right=-1):
		self.val = val
		self.left = left
		self.right = right
	
	def __hash__(self):
		return hash((self.val, self.left, self.right))

def t(n):
	return n * (n+1) // 2

def memoize(func):
	memo = {}
	def helper(tree, node):
		if node not in memo:
			memo[node] = func(tree, node)
		return memo[node]
	return helper

@memoize
def largest_sum(tree, node):
	left = node.left
	right = node.right
	if left != -1:
		return node.val + max(largest_sum(tree, tree[left]), largest_sum(tree, tree[right]))
	return node.val

with open('67.txt', 'rU') as readfile:
	nums = []
	lines = readfile.readlines()
	height = len(lines)
	for line in lines:
		nums += map(int, line.split())

nodes = []
d = 1
i = 0
while d <= height:
	for x in range(t(d), t(d+1)-1):
		if d < height:
			nodes.append(node(nums[i], x, x+1))
		else:
			nodes.append(node(nums[i]))
		i += 1
	d += 1
print(largest_sum(nodes, nodes[0]))
