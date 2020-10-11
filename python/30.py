# Digit fifth powers
# Project Euler - Problem 30
# Sean Malloy
print(sum((lambda n: n if sum(d**5 for d in map(int, map(str, str(n)))) ==
	n else 0)(i) for i in range(2, 295246)))
