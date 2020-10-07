def digit_cancel(a, b):
	str_a = str(a)
	str_b = str(b)
	
	for i in range(2):
		if str_a[i] == str_b[0]:
			return [int(str_a[(i + 1) % 2]), int(str_b[1])]
		elif str_a[i] == str_b[1]:
			return [int(str_a[(i + 1) % 2]), int(str_b[0])]
	return [a, b]

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

num_prod = 1
den_prod = 1
count = 0
for num in range(11, 100):
	if count == 4:
		break
	if num % 10 != 0:
		for den in range(11, 100):
			if count == 4:
				break
			if den % 10 != 0 and num != den:
				cancel = digit_cancel(num, den)
				if cancel[0] != num:
					if cancel[0] / cancel[1] == num / den and num / den < 1:
						num_prod *= num
						den_prod *= den

factor = gcd(num_prod, den_prod)
den_prod /= factor
print(int(den_prod))
