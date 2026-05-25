with open("Names/invited_names.txt") as file:
    content = file.read()
    content_list = content.split("\n")

    for name in content_list:
        with open("Input/letters/starting_letter.txt") as letter:
            content = letter.readlines()
            content[0] = content[0].replace("Dear [name],\n", f"Dear {name},\n")

            with open(f"Output/ReadyToSend/{name}.txt", mode="w") as final_file:
                final_file.write("".join(content))