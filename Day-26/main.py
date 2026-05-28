import pandas as pd

letter_data_frame = pd.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter: row.code for (index, row) in letter_data_frame.iterrows()}

correct_input = False

while not correct_input:
    name = input("Enter a name: ").upper()
    try:
        result_list = [phonetic_dict[letter] for letter in name]
    except KeyError:
        print("Sorry. Type only letters please")
    else:
        print(result_list)
        correct_input = True


    
    




