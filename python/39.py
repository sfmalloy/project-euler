# Integer right triangles
# Project Euler - Problem 39
# Sean Malloy
p = 1000
num_triples = {i:0 for i in range(3, p+1)}

total = 0
for a in range(1, p):
	for b in range(a+1, p):
		if a+b > p:
			break
		for c in range(b+1, p):
			if a+b+c > p:
				break
			if a**2 + b**2 == c**2:
				num_triples[a+b+c] += 1

print(max(num_triples, key = lambda a: num_triples[a]))
