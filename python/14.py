counts = {}

def collatz(n):
  if n == 1:
    return 1
  count = 1
  uncounted = {}
  while n > 1:
    count += 1
    if n in counts:
      count += counts[n]
      break
    else:
      uncounted[n] = count
    n = n/2 if n % 2 == 0 else (3*n + 1)
  # Make-shift caching for later results
  for num in uncounted:
    counts[num] = count - uncounted[num]
  return count

max_count = 0
num = 0
for i in range(2, 1000000):
  count = collatz(i)
  if max_count < count:
    max_count = count
    num = i
print(num, max_count)