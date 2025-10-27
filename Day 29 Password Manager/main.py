from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():
    passwordInput.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= randint(8,10)
    nr_symbols = randint(2,4)
    nr_numbers = randint(2,4)

    paasword_letters = [choice(letters) for _ in range(nr_letters)]
    paasword_symbols = [choice(symbols) for _ in range(nr_symbols)]
    paasword_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_characters = paasword_letters + paasword_symbols + paasword_numbers
    shuffle(password_characters)

    # Password Generator
    password = "".join(password_characters)
    passwordInput.insert(0, password)
# ---------------------------- SEARCH FOR PASSWORD ------------------------------- #
def findDetails():
    search = websiteInput.get().lower()
    with open("Day 29 Password Manager\passwords.json", "r") as file:
        data = json.load(file)

        data_keys = [key.lower() for key in data.keys()]
        if search not in data_keys:
            messagebox.showinfo(title=f"Error!", detail=f"No details for {search} exist.")

        for website in data:
            if website.lower() == search:
                user = data[website]['user']
                password = data[website]['password']
                messagebox.showinfo(title=f"Login for {website}", detail=f"Email / Username: {user}\nPassword: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def saveDetails():

    website = websiteInput.get()
    user = userInput.get()
    password = passwordInput.get()

    new_data = {
        website: {
            "user": user,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Uh oh!", message="Please don't leave any fields empty")
        return

    dialog = messagebox.askokcancel("Confirmation", message=f"Saving Details For:\nWebsite: {website}\nEmail/Username: {user}\nPassword: {password}")
    
    if dialog:
        try:
            with open("Day 29 Password Manager\passwords.json", "r") as file:
                # Read old data
                data = json.load(file)
                # Update old data with new data
                data.update(new_data)
            with open("Day 29 Password Manager\passwords.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            with open("Day 29 Password Manager\passwords.json", "w") as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)
        finally:
                websiteInput.delete(0, END)
                passwordInput.delete(0, END)


    # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

window.columnconfigure(1, weight=1) 
window.columnconfigure(2, weight=1) 

imagePath = r"Day 29 Password Manager\logo.png"
imageLogo = PhotoImage(file=imagePath)
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=imageLogo)

websiteLabel = Label(text="Website:")
websiteInput = Entry()
websiteInput.focus()
searchButton = Button(text="Search", command=findDetails)

userLabel = Label(text="Email/Username:")
userInput = Entry()
userInput.insert(0, "bigzybyron@gmail.com")

passwordLabel = Label(text="Password:")
passwordInput = Entry()
passwordGenButton = Button(text="Generate Password", command=generatePassword)

addButton = Button(text="Add", command=saveDetails)

canvas.grid(row=0, column=1)
websiteLabel.grid(row=1, column=0)
websiteInput.grid(row=1, column=1, sticky='EW') 
searchButton.grid(row=1, column=2, sticky='EW') 


userLabel.grid(row=2, column=0)
userInput.grid(row=2, column=1, columnspan=2, sticky='EW') 

passwordLabel.grid(row=3, column=0)
passwordInput.grid(row=3, column=1, sticky='EW') 
passwordGenButton.grid(row=3, column=2, sticky='EW') 

addButton.grid(row=4, column=1, columnspan=2, sticky='EW') 

window.mainloop()
