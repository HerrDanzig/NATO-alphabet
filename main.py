import pandas


with open("nato_phonetic_alphabet.csv") as nato_alphabet:
    nato_alphabet = pandas.read_csv(nato_alphabet)
    nato_dir = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

user_input = input("Words to translate: ").upper()
user_words = [word for word in user_input]

translation = []
translation = [nato_dir[letter] for letter in user_words if letter != " "]
print(translation)