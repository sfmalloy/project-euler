# Multiples of 3 and 5
# Project Euler - Problem 1
# Sean Malloy

print(sum(i for i in (set(x for x in range(3, 1000, 3)) | set(x for x in range(5, 1000, 5)))))
