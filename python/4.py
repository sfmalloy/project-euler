# Largest palindrome product
# Project Euler - Problem 4 
# Sean Malloy

# This way is more fun than converting to a string
def is_palindrome(n):
	n_copy = n
	digits = []
	pow10 = 1
	while n_copy > 0:
		digits.append(n_copy % 10)
		n_copy = n_copy // 10
	
	pow10 = 1
	while len(digits) > 0:
		d = digits[-1]
		n_copy += pow10 * d
		pow10 *= 10
		digits.pop()
	
	return n_copy == n

found = False
for a in range(999, 899, -1):
	for b in range(999, 899, -1):
		if is_palindrome(a * b):
			print(a * b)
			found = True
			break
	if found:
		break
