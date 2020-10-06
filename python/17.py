unique = ['one','two','three','four','five','six','seven','eight','nine',
		'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

length = len('onethousand')

for u in unique:
	length += len(u)

for t in tens:
	length += len(t)
	for u in unique[:9]:
		length += len(t+u)

for u in unique[:9]:
	length += len(u+'hundred')
	for u_in in unique:
		length += len(u+'hundredand'+u_in)
	for t in tens:
		length += len(u+'hundredand'+t)
		for u_in in unique[:9]:
			length += len(u+'hundredand'+t+u_in)
print(length)
