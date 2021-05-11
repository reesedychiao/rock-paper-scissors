# Print something to test if it's working.
# print to screen
print("hello")

# Ask user for their choice
# (Get user input python 2)
def play():
	weapon = raw_input("Rock, paper, or scissors? ")
	print("You entered " + weapon + "!")

# Generate computer choice
# (Generate a random choice from three options)
	import random
	options = ['rock', 'paper', 'scissors']
	counter = random.choice(options)
	print("The computer chooses " + counter + ".")

# Compare computer choice to user input
# I.E. If user said rock and computer said scissors then user wins
# (Check if two strings are the same)

	if weapon == counter :
		print("We have a tie!")

# Tell user who won
# (Print message)
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
