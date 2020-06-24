m = int(input('Enter your mark : '))
if m >= 0 and m <= 20:
	print('E')
elif m >= 21 and m <= 40:
	print('D')
elif m >= 41 and m <= 60:
	print('C')
elif m >= 61 and m <= 80:
	print('B')
else:
	print('A')