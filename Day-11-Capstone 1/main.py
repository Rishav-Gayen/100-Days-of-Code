import random
from art import logo
import os

def draw_card(card_list):
    """ Draws a random card from the card list """

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card = random.choice(cards)

    if new_card == 11 and new_card + sum(card_list) > 21:
        new_card = 1

    card_list.append(new_card)

def show_hand(user_cards, computer_cards):
    """ Shows the current score, and the cards of both the user and the computer """

    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")


def check_winner(user_cards, computer_cards):
    """ Checks win, lose or tie outcomes by comparing user cards and computer cards """

    sum_user = sum(user_cards)
    sum_computer = sum(computer_cards)

    if sum_user > 21:
        return "You lose. Bust."
    elif sum_computer > 21:
        return "You win. The Dealer went over."
    elif sum_computer == 21:
        return "You lose. The dealer has a blackjack"
    elif sum_user == 21:
        return "You win!. Blackjack!"
    elif sum_user > sum_computer:
        return "You win."
    elif sum_user < sum_computer:
        return "You lose."
    else:
        return "Tie."

def display_final_result(user_cards, computer_cards):
    """ Displays the final result of the game, shows cards, score and checks winner """

    print(f"Your final hand: {user_cards}, score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, score: {sum(computer_cards)}")
    result = check_winner(user_cards, computer_cards)
    print(result)
    


def play_game():
    """ Runs the logic of the blackjack game """
    
    print(logo)

    user_cards = []
    computer_cards = []

    for _ in range(0, 2):
        draw_card(user_cards)
    
    draw_card(computer_cards)
    
    keep_drawing = True

    while keep_drawing:
        show_hand(user_cards, computer_cards)
        choice = input("Type 'y' to get another card, type 'n' to pass: ")

        if choice == 'n':
            keep_drawing = False
        else:
            draw_card(user_cards)
            if sum(user_cards) >= 21:
                keep_drawing = False
                display_final_result(user_cards, computer_cards)
                return

    while sum(computer_cards) < 17:
        draw_card(computer_cards)
    
    display_final_result(user_cards, computer_cards)
    
game_is_on = True

while game_is_on:
    user_choice = input("Do you want to play a game of blackjack? Type 'y' for yes and 'n' for no: ")
    if user_choice == 'n':
        game_is_on = False
    else:
        os.system('cls')
        play_game()

