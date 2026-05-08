from art import logo

def caesar_cipher(plaintext, shift, action):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cipher_text = ""

    for char in plaintext:

        if char.lower() in letters:

            letter_position = letters.index(char.lower())

            if action == 'encode':
                cipher_char = letters[(letter_position + shift) % len(letters)]
            else:
                cipher_char = letters[(letter_position - shift) % len(letters)]

            if char.isupper():
                cipher_text += cipher_char.upper()
            else:
                cipher_text += cipher_char

        else:
            cipher_text += char

    print(f"Your {action}d text is {cipher_text}")


program_is_on = True

while program_is_on:
    print(logo)

    action = input("Type encode to encrypt type decode to decrypt\n")
    message = input("Type your message\n")
    shift = int(input("Type your shift number\n"))

    caesar_cipher(message, shift, action)

    choice = input("Type yes if you want to continue, else type no\n")

    if choice.lower() == "no":
        program_is_on = False
    



