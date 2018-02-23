import random
def compare():
	
	while True:
		a1 = int(raw_input("Please enter 1 for rock, 2 for paper, or 3 for scissors. "))
		if a1 in (1,2,3):
			break
		print("Please enter only 1, 2, or 3")
	a2 = random.randint(1,3)
	names = ["Blank", "rock", "paper", "scissors"]
	win = ("Congratulations, you won!")
	loss = ("Sorry, you lost.")
	draw = ("Draw")
	rock = 1
	paper = 2
	scissors = 3
	if a1 == a2:
		print(draw)
	elif a1 == 1 and a2 == 2:
		print(loss)
	elif a1 == 1 and a2 == 3:
		print(win)
	elif a1 == 2 and a2 == 1:
		print(win)
	elif a1 == 2 and a2 == 3:
		print(loss)
	elif a1 == 3 and a2 == 1:
		print(loss)
	elif a1 == 3 and a2 == 2:
		print(win)
	else:
		print("My code sucks")
	print("You chose " + names[a1])
	print("The computer chose " + names[a2])



while True:
	compare()
	while True:
		answer = raw_input("Would you like to play again? (y/n): ")
		if answer in ("y","n"):
			break
		print("Please try again")
	if answer == "y":
		continue
	else:
		print("Thanks for playing")
		break

