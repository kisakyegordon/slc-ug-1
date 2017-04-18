
print("\nSLC-UG Day 1 Task\n")


def print_prime():
	n = 20
	#print(int(input))
	for p in range(2, n+1):
		for i in range(2, p):
			if p % i == 0:
				break
		else:
			print p,
	print('\nDone')
	
print_prime()
