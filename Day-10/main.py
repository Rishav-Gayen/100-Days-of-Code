from art import logo
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

calculator_is_on = True

while calculator_is_on:
    operation = ""
    running_total = 0
    next_number = 0

    print(logo)
    number = float(input("What is the first number?: "))

    keep_calculating = True

    while keep_calculating:

        for symbol in operations:
            print(symbol)

        wrong_input = True

        while wrong_input:
            operation = input("Pick an operation: ")
            if operation in operations.keys():
                wrong_input = False

        next_number = float(input("What is the next number?: "))

        running_total = operations[operation](number, next_number)
    
        print(f"{number} {operation} {next_number} = {running_total}")
        number = running_total

        choice = input("Do you wanna keep calculating? Type 'y' for yes and 'n' for no: ")

        if choice == 'n':
            keep_calculating = False

    print(f"Your final result is {number}.")
    quit_flag = input("Do you want to quit ? Type 'y' for yes and 'n' for no: ")

    if quit_flag == 'y':
        calculator_is_on = False
    else:
        os.system('cls')






    


