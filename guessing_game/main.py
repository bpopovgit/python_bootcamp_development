import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
game_difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")
is_game_over = False


def check_difficulty(game_difficulty_):
    attempts_remaining = -1
    if game_difficulty_ == 'easy':
        attempts_remaining = 10
    elif game_difficulty_ == 'hard':
        attempts_remaining = 5
    return attempts_remaining


attempts = check_difficulty(game_difficulty)

print(f"You have {attempts} attempts remaining to guess the number.")

while not is_game_over:
    guess = int(input("Make a guess: "))
    if guess != number and guess < number:
        attempts -= 1
        if attempts <= 0:
            print("You ran out of attempts!")
            is_game_over = True
        if not is_game_over:
            print(f"You have {attempts} attempts remaining to guess the number.")
            print(f"Too low.\nGuess again.")
    elif guess != number and guess > number:
        attempts -= 1
        if attempts <= 0:
            print("You ran out of attempts!")
            is_game_over = True
        if not is_game_over:
            print(f"You have {attempts} attempts remaining to guess the number.")
            print(f"Too high.\nGuess again.")

    elif guess == number:
        print(f"You got it! The answer was {number}.")
        is_game_over = True
