from art import logo, word_bank, HANGMANPICS
import random

random_word = random.choice(word_bank)
game_is_on = True
user_guesses = []
total_lives = 6
user_lives = total_lives

display_word = []
for i in range(0, len(random_word)):
    display_word.append("_")

print(logo)

while game_is_on:
    print("Word to guess ", end="")
    
    for char in display_word:
        print(char, end="")
    
    print("\n")
    guess = input("Guess a letter: ")

    if guess in user_guesses:
        print(f"You've already guessed {guess}")
    elif guess not in random_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        user_lives -= 1
    else:
        for i in range(0, len(random_word)):
            if guess == random_word[i]:
                display_word[i] = guess
                user_guesses.append(guess)

    if user_lives < 1 or len(user_guesses) == len(random_word):
        game_is_on = False
    else:
        print(HANGMANPICS[6 - user_lives])
        print(f"****************** {user_lives}/{total_lives} LIVES LEFT ***************")

if user_lives > 0:
    print(f"**************** IT WAS {random_word}! YOU WIN *******************")
else:
    print(f"**************** IT WAS {random_word}! YOU LOSE *********************")
        

    