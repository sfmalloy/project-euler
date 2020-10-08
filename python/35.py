LIMIT = 1000000
primes = [True for _ in range(LIMIT)]
primes[0] = primes[1] = False

for i in range(2, len(primes)):
	if primes[i]:
		step = i
		index = i + step
		while index < len(primes):
			primes[index] = False
			index += step

def rotate(p):
	return str(p)[1:] + str(p)[0]

def is_circular(p):
	rot = rotate(p)
	for _ in range(len(str(p))):
		if not primes[int(rot)]:
			return False
		rot = rotate(rot)
	return True

count = 0
for p in range(2, len(primes)):
	if primes[p] and is_circular(p):
		count += 1
print(count)
