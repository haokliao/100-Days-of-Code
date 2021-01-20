#Step 5
import random
from Day7_hangman_game_art import stages,logo
from Day7_hangman_game_words import word_list


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f'You\'ve already guessed {guess}')
      
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. Life -1")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOSE.")

    print(f"{' '.join(display)}")
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])