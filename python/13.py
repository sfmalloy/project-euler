with open('13.txt', 'r') as readfile:
    print(str(sum(int(line) for line in readfile.readlines()))[:10])