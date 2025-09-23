alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrpyt, type 'decode' to decrypt:\n").lower() 
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Combine this into a single function
'''
def encrypt(text, shift):
    result = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = (position + shift) % 26
        result += alphabet[new_position]

    print(f"Your encrypted message is: {result}")

def decrypt(text, shift):
    result = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = (position - shift) % 26
        result += alphabet[new_position]

    print(f"Your decrypted message is: {result}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Sorry, but that's not a valid option.")
'''

# Single Function Version
def caesar(original_text, shift_amount, encode_or_decode):
    result = ""
    for letter in original_text:
        if not letter.isalpha():
            result += letter
            continue

        if encode_or_decode == "decode":
            shift_amount *= -1

        position = alphabet.index(letter)
        new_position = (position + shift_amount) % 26
        result += alphabet[new_position]

    print(f"Your {encode_or_decode}d message is: {result}")
    
caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
