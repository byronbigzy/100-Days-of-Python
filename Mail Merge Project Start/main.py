import os

# Get Names
with open(file="Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as names:
    list_names = []
    for line in names.readlines():
        list_names.append(line.strip("\n"))

for name in list_names:
    with open(file=f"Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", mode="x") as newLetter:
        with open(file="Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as template:
            for line in template.readlines():
                newLetter.write(line.replace("[name]", name))