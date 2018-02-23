def get_integer():
	return int(raw_input("Please type a number and press ENTER  "))
	
def check_prime(x):
	prime = 0
	for element in range(2,(x)):
		if x % element == 0:
			prime = 1
		elif prime == 0:
			continue
	if prime == 0:
		print("Your number is prime.")
	else:
		print("Your number is non-prime.")

def start_loop():	
	while True:
		check_prime(get_integer())
		while True:
			usr_inpt = raw_input("Would you like to try another number? (y/n)  ")
			if usr_inpt in ("y","n"):
				break
			print("Please try again")
		if usr_inpt == "y":
			continue
		else:
			print("Thanks for using Jack's PrimeCheck!")
			break
		
start_loop()

				






