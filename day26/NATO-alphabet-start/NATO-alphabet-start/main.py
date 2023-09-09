import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
Nato = []
print(data_frame)
Nato = {row.letter: row.code for (index,row) in data_frame.iterrows()}
print(Nato)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
userInput= input("Enter a word").upper()
Output_list = [Nato[letter] for letter in userInput]
print(Output_list)