# Coded triangle numbers
# Project Euler - Problem 42
# Sean Malloy
from math import sqrt

def alpha_val(word):
	val = 0
	for w in word:
		val += ord(w) - 64
	return val

def is_triangle(T):
	return ((1 + sqrt(1 + 8*T)) / 2) % 1 == 0

with open('042.txt', 'r') as readfile:
	words = [w.strip('\"') for w in readfile.readline().split(',')]

count = 0
for w in words:
	if is_triangle(alpha_val(w)):
		count += 1
print(count)
