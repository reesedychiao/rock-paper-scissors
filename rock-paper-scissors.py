print("hello")


def play():
	weapon = raw_input("Rock, paper, or scissors? ")
	print("You entered " + weapon + "!")
	import random
	options = ['rock', 'paper', 'scissors']
	counter = random.choice(options)
	print("The computer chooses " + counter + ".")

	if weapon == counter :
		print("We have a tie!")
	elif weapon == 'rock' and counter == 'paper' :
		print("Paper beats rock. You lose :(")
	elif weapon == 'paper' and counter == 'rock' :
		print("Paper beats rock. You win!")
	elif weapon == 'rock' and counter == 'scissors' :
		print("Rock beats scissors. You win!")
	elif weapon == 'scissors' and counter == 'rock' :
		print("Rock beats scissors. You lose :(")
	elif weapon == 'paper' and counter == 'scissors' :
		print("Scissors beats paper. You lose :(")
	elif weapon == 'scissors' and counter == 'paper' :
		print("Scissors beats paper. You win!")
	else:
		print("Try again :(")
	

	if (weapon == 'exit'):
		exit()

	play ()

play()
