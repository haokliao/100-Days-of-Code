#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


import random
EASY_LIVES = 10
HARD_LIVES = 10

def mode():
	#sets difficulty level, assigns global mode to 
		difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ').lower()
		if difficulty == 'easy':
			return EASY_LIVES
		if difficulty == 'hard':
			return HARD_LIVES

def checker(guess, answer, lives):
	#keeps track of lives
	if guess > answer:
		print('Too high!') 
		return lives -1
	elif guess < answer:
		print('Too low!')
		return lives -1
	else:
		print(f'You win! the answer is {answer}') 

def game():
	print('Welcome to the Number Guessing Game!')
	print('I\'m thinking of a number between 1 and 100.')
	answer = random.randrange(0,101)
	# print(answer)

	lives = mode()
	#assigns lives, pulls value of EASY_LIVES into the function mode(), so you can subtract lives from there.
	#instead of using global variable
	
	guess = 0
	#need to assign a variable to guess to use for while loop

	while guess != answer:
		print(f'You have {lives} attempts to guess the answer!')
		guess = int(input('Make a guess: '))

		lives = checker(guess,answer,lives)
		if lives == 0:
			print('You\'ve run out of lives! You LOSE')
			return
		elif guess != answer:
			print('Try again.')

game()