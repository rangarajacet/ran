while True:
	print("Enter 'x' for exit.")
	num = input("Enter year: ")
	if num == 'x':
		break
	try:
		year = int(num)
	except ValueError:
		print("Please, enter year...")
	else:
		if((year%4 == 0) and (year%100 != 0)):
			print(year, "it is a Leap Year.\n")
		elif(year%100 == 0):
			print(year, "it is not a Leap Year.\n")
		elif(year%400 == 0):
			print(year, "it is a Leap Year.\n")
		else:
			print(year, "it is not a Leap Year.\n")
