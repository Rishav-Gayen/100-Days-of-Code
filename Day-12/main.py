from art import logo
import random

def play_game():
    random_number = random.randint(1, 100)
    lives = 0
    game_is_on = True
    user_guess = 0

    print(logo)

    print("\n")

    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty.lower() == 'easy':
        lives = 10
    else:
        lives = 5

    while game_is_on and lives > 0:
        print(f"You have {lives} attempts to guess the number")
        user_guess = int(input("Make a guess: "))

        if user_guess > random_number and lives > 1:
            lives -= 1
            print("Too High.\nGuess Again.")
        elif user_guess < random_number and lives > 1:
            lives -= 1
            print("Too Low.\nGuess Again.")
        else:
            game_is_on = False

    if user_guess == random_number:
        print(f"You got it! It was {random_number}")
    else:
        print(f"You have run out of guesses. It was {random_number}")
        
    

play_game()

    

