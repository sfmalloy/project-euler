# Lattice paths
# Project Euler - Problem 15
# Sean Malloy
MAX_X = MAX_Y = 20

def memoize(func):
  memo = {}
  def helper(x, y):
    if (x, y) not in memo:
      memo[(x, y)] = func(x, y)
    return memo[(x, y)]
  return helper

@memoize
def find_path(x, y):
  if x > MAX_X or y > MAX_Y:
    return 0
  if x == MAX_X and y == MAX_Y:
    return 1
  return find_path(x + 1, y) + find_path(y + 1, x)
print(find_path(0, 0))
