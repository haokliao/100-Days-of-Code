from art import logo
from gamedata import data
import random

def formatted(choice):
    """Create a function that allows you to input choice and fetch the data"""
    choice_name = choice['name']
    choice_desc = choice['description']
    choice_country = choice['country']
    return (f"{choice_name}, a {choice_desc}, from {choice_country}.")

def checker (guess, a_followers, b_followers):
    """checks if guess is correct"""
    if guess == 'a' and a_followers > b_followers:
        return True
    elif guess == 'b' and b_followers > a_followers:
        return True
    else:
        return False

gamestart = True
score = 0
choice_A = random.choice(data)
choice_B = random.choice(data)

#repeatable
while gamestart:
    #choice A should be the version which was at choice B
    # prints choice and your compare statements
    print(logo)
 
    while choice_B == choice_A:
        choice_B = random.choice(data)

    print(f'Compare A: {formatted(choice_A)}')
    print('vs')
    print(f'Against B: {formatted(choice_B)}')

    # #follower count
    a_followers = choice_A['follower_count']
    
    b_followers = choice_B['follower_count']
    print(a_followers,b_followers)
    #ask user for a guess
    guess = input('Who has more followers? Type \'A\' or \'B\': ').lower()

    #clear screen 
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

    #check if user is correct
    correct = checker(guess,a_followers,b_followers)

    #give user feedback, overwrites choice a with the correct answer.
    if correct :
        score += 1
        print(f'CORRECT, your score is {score}')
        if b_followers > a_followers:
            choice_A = choice_B
            choice_B = random.choice(data)
        else:
            choice_B = choice_A
    else:
        print(f'C\'mon dawg , your final score is {score} ')
        gamestart = False
