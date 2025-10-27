from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def saveDetails():
    try:
        with open("Day 29 Password Manager\passwords.txt", "a") as file:
            file.write(f"{websiteInput.get()} | {userInput.get()} | {passwordInput.get()}\n") 
    except FileNotFoundError:
        file = open("Day 29 Password Manager\passwords.txt", "w")
        file.write(f"{websiteInput.get()} | {userInput.get()} | {passwordInput.get()}\n") 
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

userLabel = Label(text="Email/Username:")
userInput = Entry()
userInput.insert(0, "bigzybyron@gmail.com")

passwordLabel = Label(text="Password:")
passwordInput = Entry()
generatePassword = Button(text="Generate Password")

addButton = Button(text="Add", command=saveDetails)

canvas.grid(row=0, column=1)
websiteLabel.grid(row=1, column=0)
websiteInput.grid(row=1, column=1, columnspan=2, sticky='EW') 

userLabel.grid(row=2, column=0)
userInput.grid(row=2, column=1, columnspan=2, sticky='EW') 

passwordLabel.grid(row=3, column=0)
passwordInput.grid(row=3, column=1, sticky='EW') 
generatePassword.grid(row=3, column=2, sticky='EW') 

addButton.grid(row=4, column=1, columnspan=2, sticky='EW') 

window.mainloop()
