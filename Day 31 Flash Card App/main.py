from tkinter import *
import pandas as pd
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"
FLIP_COLOR = "#91c2af"
LANG_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

# Get Words
try:
    data = pd.read_csv("Day 30 Flash Card App\data\words_to_learn.csv")
    print("Words to learn found")
except FileNotFoundError:
    data = pd.read_csv("Day 30 Flash Card App\data\czech_words.csv")
    print("Backup Czech Words")

data_dict = data.to_dict(orient="records")
current_word = None
transition = None

def refreshWord():
    flashcard.itemconfig(card, image=card_front)
    global current_word
    current_word = random.choice(data_dict)
    word_text.config(text=f"{current_word['Czech']}", fg="black", bg="white")
    lang_text.config(text='Czech', fg="black", bg="white")
    global transition
    transition = window.after(3000, flipCard)

def flipCard():
    flashcard.itemconfig(card, image=card_back)
    word_text.config(text=f"{current_word['English']}", fg="white", bg=FLIP_COLOR)
    lang_text.config(text='English', fg="white", bg=FLIP_COLOR)

def knownWord():
    global transition
    window.after_cancel(transition)
    data_dict.remove(current_word)
    df = pd.DataFrame.from_dict(data_dict)
    df.to_csv("Day 30 Flash Card App\data\words_to_learn.csv")
    refreshWord()

# UI Setup
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back = PhotoImage(file=r"Day 30 Flash Card App\images\card_back.png")
card_front = PhotoImage(file=r"Day 30 Flash Card App\images\card_front.png")
right = PhotoImage(file=r"Day 30 Flash Card App\images\right.png")
wrong = PhotoImage(file=r"Day 30 Flash Card App\images\wrong.png")

flashcard = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = flashcard.create_image(400, 263, image=card_front)
lang_text = Label(text="Czech", font=LANG_FONT)
word_text = Label(text="Word", font=WORD_FONT)
right_button = Button(image=right, command=knownWord, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_button = Button(image=wrong, command=refreshWord, bg=BACKGROUND_COLOR, highlightthickness=0)

flashcard.grid(row=0, column=0, columnspan=2)
lang_text.place(x=400, y=150, anchor="center")
word_text.place(x=400, y=263, anchor="center")
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

refreshWord()

window.mainloop()