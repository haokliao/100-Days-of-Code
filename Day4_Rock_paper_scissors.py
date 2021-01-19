import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock,paper,scissors]
print('Welcome to Rock Papers Scissors!')


player_choice = int(input('Type 0 for Rock, 1 for Paper, 2 for Scissors. '))
if player_choice >= 3 or player_choice < 0:
  print('Keep numbers between 0-2!')
else:
  print(choices[player_choice])
  computer_choice = (random.randint(0,2))
  print(f'The computer chooses: {choices[computer_choice]}')
  if player_choice == 0 and computer_choice == 2:
    print('Player wins')
  elif computer_choice > player_choice:
    print('You lose')
  elif player_choice > computer_choice:
    print('You win')
  elif player_choice == computer_choice:
    print('It\'s a draw!')
