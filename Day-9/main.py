import os
from art import logo

# Clear Screen os.system('cls')
def find_highest_bidder(bidding_dictionary):
    winner_name = ""
    max_bid = 0

    for contestant in bidding_dictionary:
        if bidding_dictionary[contestant] > max_bid:
            max_bid = bidding_dictionary[contestant]
            winner_name = contestant

    print(f"The winner is {winner_name} with a bid of ${max_bid}")

bidders = {}
program_is_on = True

print("Welcome to the secret auction program.")
print(logo)

while program_is_on:

    contestant_name = input("What is your name?: ")
    contestant_bid = int(input("What is your bid?: $"))

    bidders[contestant_name] = contestant_bid

    proceed = input("Are there any other bidders? Type 'yes' or 'no'\n")

    if proceed.lower() == 'no':
        program_is_on = False

    else:
        os.system('cls')

os.system('cls')
find_highest_bidder(bidders)

