# Truncatable primes
# Project Euler - Problem 37
# Sean Malloy
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

def truncate_lr(p):
	return '' if len(str(p)) == 1 else str(p)[1:]

def truncate_rl(p):
	return '' if len(str(p)) == 1 else str(p)[0:-1]

def is_truncate(p):
	lr = truncate_lr(p)
	rl = truncate_rl(p)
	while lr != '':
		if not primes[int(lr)] or not primes[int(rl)]:
			return False
		lr = truncate_lr(lr)
		rl = truncate_rl(rl)
	return True

s = 0
for p in range(11, len(primes)):
	if primes[p] and is_truncate(p):
		s += p
print(s)
