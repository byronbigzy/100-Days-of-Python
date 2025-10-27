import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters= random.randint(8,10)
nr_symbols = random.randint(8,10)
nr_numbers = random.randint(8,10)

chosen_characters = []

for i in range(0, nr_letters):
    chosen_characters.append(random.choice(letters))

for i in range(0, nr_symbols):
    chosen_characters.append(random.choice(symbols))

for i in range(0, nr_numbers):
    chosen_characters.append(random.choice(numbers))

random.shuffle(chosen_characters)

# Password Generator
password = "".join(chosen_characters)
