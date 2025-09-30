import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
number = random.randint(1,100)
attempts = 0

guessing = False

while not guessing:
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        difficulty = input("Your input was invalid.\nChoose a difficulty. Type 'easy' or 'hard': ")
        continue
    guessing = True

while guessing and attempts > 0:
    print(f"You have {attempts} attempts remaining.")
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    elif guess == number:
        print(f"You got it! The answer was {number}")
        break
    attempts -= 1

if attempts == 0:
    print(f"You've run out of guesses. The number was {number}. You lose.")