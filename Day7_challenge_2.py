#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

guess = input("Guess a letter: ").lower()
display = []
for letter in chosen_word:
  display.append("_")
print(display)
#loops through chosen word, adding a _ to each letter in that word.


#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#loops through the range of the length of chosen word, which gets all position indexes in word
#create letter, equal to current position in chosen word
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
      #gets item at the current position, and appends it to letter.


#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
print(display)