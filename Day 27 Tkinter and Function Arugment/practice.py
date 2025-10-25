from tkinter import *

# Creating a new window
window = Tk()
window.title("Mile to KM convertor")

FONT = ("Arial", 24, "bold")

# Miles Input
input = Entry()
input.grid(column=2, row=1)

# Miles Label
miles_label= Label(text="Miles")
miles_label.grid(column=3, row=1)

# Is Equal To
equal_label= Label(text="is equal to")
equal_label.grid(column=1, row=2)

# Result in KM
km_result= Label(text="0")
km_result.grid(column=2, row=2)

# KM Label
km_label= Label(text="Km")
km_label.grid(column=3, row=2)

# Button
def button_clicked():
    if (input.get() == ""):
        return
    km_result.config(text=f"{int(input.get())*1.609}")

button = Button(text="Calculate", command=button_clicked)
button.grid(row=3, column=2)

#Keep window running
window.mainloop()