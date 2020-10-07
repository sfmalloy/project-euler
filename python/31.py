s = 1
goal = 201
for pence in range(0, goal):
	for twopence in range(0, goal - pence, 2):
		for fivepence in range(0, goal - pence - twopence, 5):
			for tenpence in range(0, goal - pence - twopence - fivepence, 10):
				for twentypence in range(0, goal - pence - twopence - fivepence - tenpence, 20):
					for fiftypence in range(0, goal - pence - twopence - fivepence
							- tenpence - twentypence, 50):
						for pound in range(0, goal - pence - twopence - fivepence
								- tenpence - twentypence - fiftypence, 100):
							curr = sum([pence, twopence, fivepence, tenpence, twentypence,
									fiftypence, pound])
							if curr == 200:
								s += 1

print(s)
