from math import sqrt
def div_count(num):
  count = 0
  for i in range(1, int(sqrt(num)) + 1):
    if num % i == 0:
      count += 1
      # Check other divisor by dividing num by i
      # If other divisor is not the same as i then
      #   it is another unique divisor you can count.
      if num / i != i:
        count += 1
  return count


i = 2
num = 1
x = div_count(num)
while x < 500:
  num += i
  i += 1
  x = div_count(num)
print(num)