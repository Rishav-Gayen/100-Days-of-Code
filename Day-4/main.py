import random

# Rock Paper Scissors ASCII Art

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice_list = [rock, paper, scissors]


user_choice = int(input("What do you choose ? Type 0 for rock, 1 for paper, or 2 for scissors\n"))

if user_choice >= 0 and user_choice <= 2:

    print(choice_list[user_choice])
    computer_choice = random.randint(0, 2)

    print("Computer Chose")
    print(choice_list[computer_choice])

    if user_choice == computer_choice:
        print("Tie")
    elif computer_choice == 2 and user_choice == 0:
        print("You win")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif user_choice > computer_choice:
        print("You Win")
    else:
        print("You Lose")
else:
    print("Out of bounds.")
