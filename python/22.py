# Names scores
# Project Euler - Problem 22 
# Sean Malloy
def alpha_val(name):
	score = 0
	for c in name:
		score += ord(c) - 64
	return score

with open('22.txt', 'r') as readfile:
	names = sorted([name.strip('\"') for name in readfile.readline().split(',')])

total = 0
for i in range(len(names)):
	total += alpha_val(names[i]) * (i + 1)
print(total)
