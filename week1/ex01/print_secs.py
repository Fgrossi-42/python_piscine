import sys

if len(sys.argv) == 4:
	try:
		n1 = int(sys.argv[1])
		n2 = int(sys.argv[2])
		n3 = int(sys.argv[3])
		print((n1 * (60 ** 2)) + n2 * 60 + n3)
	except:
		print("Wrong value!")
else:
	print("Wrong arguments!")

