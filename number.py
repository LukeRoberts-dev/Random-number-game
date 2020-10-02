def main():

	import random
	
	yesList = ["yes", "yeah", "y", "yea", "yee"]
	hidden = int(random.randrange(0, 20))


	guess = int(input("Guess a number between 0 and 20.\n"))
	if guess == hidden:
		print("Correct!! The number was", hidden)
	elif guess < hidden:
		print("Sorry you were incorrect. The number was", hidden)
	else:
		print("Sorry you were incorrect. The number was", hidden)


	restart = str(input("Would you like to restart?\n"))
	if restart in yesList:
		main()
	else:
		exit()

main()
