import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

words = ["alphabet", "game", "jazz"]

lives = len(stages) - 1

# Select a word @ random
chosen_word = random.choice(words)

print(chosen_word)

# Placeholder Generator:
placeholder = len(chosen_word)*"_"
print(placeholder)

game_over = False
correct_letters = []
while not game_over:
    # Player guess
    guess = input("Guess a letter: ").lower()

    # Display Correct Guesses:
    display = ""

    # Update Display
    for letter in chosen_word:
        if letter == guess:
            display += guess
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess in chosen_word:
        print("Correct!")
        correct_letters.append(guess)
    else:
        print("Wrong!")
        lives -= 1
        if lives == 0:
            game_over = True
            print(stages[lives])
            print("You've lost all your lives, GAME OVER!")
            print("The word was:", chosen_word)
            break
        else:
            print(f"You've lost a life, You now have {lives} lives remaining.")
    
    print(stages[lives])
    print(display)

    # Victory
    if display == chosen_word:
        game_over = True
        print("You've correctly guessed the word!\nYou win!")