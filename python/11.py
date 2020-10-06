with open('11.txt', 'r') as readfile:
  lines = [list(map(int, line.split())) for line in readfile.readlines()]

PROD_LENGTH = 4
def horiz(lines):
  prod = 1
  for i in range(len(lines)):
    for j in range(len(lines) - PROD_LENGTH):
      temp = 1
      for k in range(j, j + PROD_LENGTH):
        temp *= lines[i][k]
      prod = max(temp, prod)
  return prod

def vert(lines):
  prod = 1
  for i in range(len(lines) - PROD_LENGTH):
    for j in range(len(lines)):
      temp = 1
      for k in range(i, i + PROD_LENGTH):
        temp *= lines[k][j]
      prod = max(temp, prod)
  return prod

def left_right(lines):
  prod = 1
  for i in range(len(lines) - PROD_LENGTH + 1):
    for j in range(len(lines) - PROD_LENGTH + 1):
      temp = 1
      for k in range(PROD_LENGTH):
        elem = lines[i+k][j+k]
        temp *= elem
      prod = max(temp, prod)
  return prod

def right_left(lines):
  prod = 1
  for i in range(len(lines) - PROD_LENGTH + 1):
    for j in range(len(lines) - PROD_LENGTH + 1):
      temp = 1
      l = PROD_LENGTH - 1
      for k in range(PROD_LENGTH):
        elem = lines[i+l][j+k]
        temp *= elem
        l -= 1
      prod = max(temp, prod)
  return prod

print(max(horiz(lines), vert(lines), left_right(lines), right_left(lines)))