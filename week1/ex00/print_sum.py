import sys

if len(sys.argv) == 3:
	try:
		n1 = int(sys.argv[1])
		n2 = int(sys.argv[2])
		sum = n1+n2
		print(sum)
	except:
		print("Wrong value!")
else:
	print("Wrong arguments!")
