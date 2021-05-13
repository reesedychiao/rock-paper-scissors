print("hello")

score = {"user":0, "computer":0}


def play(score):
	weapon = raw_input("Rock, paper, or scissors? ")
	print("You entered " + weapon + "!")

	if (weapon == 'exit'):
		exit()

	import random
	options = ['rock', 'paper', 'scissors']
	counter = random.choice(options)
	print("The computer chooses " + counter + ".")


	if weapon == counter :
		print("We have a tie!")
	elif weapon == 'rock' and counter == 'paper' :
		print("You lose :(")
		score["computer"] += 1
	elif weapon == 'paper' and counter == 'rock' :
		print("You win!")
		score["user"] += 1
	elif weapon == 'rock' and counter == 'scissors' :
		print("You win!")
		score["user"] += 1
	elif weapon == 'scissors' and counter == 'rock' :
		print("You lose :(")
		score["computer"] += 1
	elif weapon == 'paper' and counter == 'scissors' :
		print("You lose :(")
		score["computer"] += 1
	elif weapon == 'scissors' and counter == 'paper' :
		print("You win!")
		score["user"] += 1
	else:
		print("Try again :(")

	raw_user_score = int(score["user"])
	user_string = str(raw_user_score)

	raw_computer_score = int(score["computer"])
	computer_string = str(raw_computer_score)

	print("Your score: " + user_string + " \nComputer's score: " + computer_string + "")


	play (score)

play(score)
