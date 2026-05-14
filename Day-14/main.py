from art import logo, vs
from gamedata import data
import os
import random

# Get random person

def get_random_person():
    return random.choice(data)
            

# Compare Both followers
def check_winner(person_a, person_b):
    follower_a = person_a["follower_count"]
    follower_b = person_b["follower_count"]

    if follower_a > follower_b:
        return person_a
    elif follower_a < follower_b:
        return person_b
    else:
        return person_b
    
def get_user_input():
    correct_input = False
    while not correct_input:
        choice = input("Who has more followers? Type A or B: ")
        if choice.upper() == 'A':
            return 'A'
        elif choice.upper() == 'B':
            return 'B'
        else:
            print("Invalid Input")

# Check answers
def check_answer(user_answer, winner):
    return user_answer == winner

def play_game():
    game_is_on = True
    person_a = get_random_person()
    user_score = 0

    while game_is_on:
        os.system('cls')
        print(logo)
    
        person_b = get_random_person()

        winner = check_winner(person_a, person_b)

        if user_score > 0:
            print(f"You're right! Current score: {user_score}")

        print(f"Compare A: {person_a["name"]}, a {person_a["description"]}, from {person_a["country"]} - F {person_a["follower_count"]}")
        print(vs)
        print(f"Compare B: {person_b["name"]}, a {person_b["description"]}, from {person_b["country"]} - F {person_b["follower_count"]}")

        user_choice = get_user_input()

        if user_choice == 'A':
            user_choice = person_a
        else:
            user_choice = person_b

        if check_answer(user_choice, winner):
            person_a = person_b
            user_score += 1
            print(f"You're right! Current score: {user_score}")
        else:
            game_is_on = False

    os.system('cls')
    print(logo)
    print(f"Sorry that's wrong. Final score: {user_score}")

play_game()


    

    
            
    



