
# Gets integet from user

def get_integer():
	return int(input("Please type a number and press ENTER  "))
	
# Checks if number is prime, and prints the factors of non-prime inputs

def check_prime(x):
	factor_list = []
	prime = 0
	if x > 15000000:
		print("Your number is too large for your hardware to factor")
	else:
		for element in range(2,(x)):
			if x % element == 0:
				factor_list.append(element)
				prime = 1
			elif prime == 0:
				continue
		if prime == 0:
			print("Your number is prime.")
		else:
			print("Your number is non-prime.")
			print("The factors of your number are " + str(factor_list))

# Nests check_prime function into a loop that prompts user to restart

def start_loop():	
	while True:
		check_prime(get_integer())
		while True:
			usr_inpt = input("Would you like to try another number? (y/n)  ")
			if usr_inpt in ("y","n"):
				break
			print("Please try again")
		if usr_inpt == "y":
			continue
		else:
			print("Thanks for using Jack's PrimeCheck!")
			break
		
start_loop()	






