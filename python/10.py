upper = 2000000
is_prime = [True for i in range(upper + 1)]
is_prime[0] = is_prime[1] = False

for i in range(2, upper+1):
    index = step = i
    if is_prime[index]:
        index += step
        while index <= upper:
            is_prime[index] = False
            index += step

s = 0
for i in range(2, upper+1):
    if is_prime[i]:
        s += i
print(s)