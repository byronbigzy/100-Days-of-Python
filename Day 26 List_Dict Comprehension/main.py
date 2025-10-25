import pandas as pd

path = r"Day 26 List_Dict Comprehension\nato_phonetic_alphabet.csv"

nato_csv = pd.read_csv(path)
df = pd.DataFrame(nato_csv)

nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

name = input("Enter your name: ")

name_list = [nato_dict[letter.upper()] for letter in name]

print(name_list)