import random

x = random.randint(1,9)
winner = 0

def guess():
	global x
	global winner
	usr_inpt = int(raw_input("Please enter a number between 1 and 9  "))
	if usr_inpt == x:
		print("You are a winner!")
		x = random.randint(1,9)
		winner = 1
	elif usr_inpt > x:
		print("Your guess is high")
	else:
		print("Your guess is low")
	

while True:
	guess()
	if winner == 0:
		continue
	else:
		answer = raw_input("Would you like to play again? (y/n) ")
		if answer in ("y","n") and answer == "y":
			continue
		else:
			print("Thanks for playing!")
			break
		
