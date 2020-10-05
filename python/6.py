print((lambda limit: (int(limit * (limit+1) / 2)**2 - (sum(i**2 for i in range(1,
	limit+1)))))(100))
