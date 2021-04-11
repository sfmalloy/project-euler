# Large sum
# Project Euler - Problem 13
# Sean Malloy
with open('013.txt', 'r') as readfile:
    print(str(sum(int(line) for line in readfile.readlines()))[:10])
