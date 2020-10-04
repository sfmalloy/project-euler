N = int(input())
factor = 2
while N > 1:
	if N % factor == 0:
		N /= factor
	if N > 1:
		factor += 1 if factor == 2 else 2
print(int(factor))
