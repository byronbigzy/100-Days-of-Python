from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
    window.after_cancel(timer)
    canvas.itemconfig(timerText, text="00:00", fill="white",font=(FONT_NAME, 24, "bold"))
    timerLabel.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
    checkmarkLabel.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timerLabel.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        countdown(short_break_sec)
        timerLabel.config(text="Break", fg=PINK)

    else:
        countdown(work_sec)
        timerLabel.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10: 
        count_sec = f"0{count_sec}"

    if count_min < 10: 
        count_min = f"0{count_min}"

    canvas.itemconfig(timerText, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        if reps % 2 == 0:
            checkmarkLabel.config(text="✔"*(reps//2))
        startTimer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Pomodoro Image and Text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoroImg = PhotoImage(file=r"Day 28 Pomodoro\tomato.png")
canvas.create_image(100, 112, image=pomodoroImg)
timerText = canvas.create_text(103,130, text="00:00", fill="white",font=(FONT_NAME, 24, "bold"))

timerLabel = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
startButton = Button(text="Start", highlightthickness=0, command=startTimer)
resetButton = Button(text="Reset", highlightthickness=0, command=resetTimer)
checkmarkLabel = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))

timerLabel.grid(row=0, column=1)
canvas.grid(row=1, column=1)
startButton.grid(row=3, column=0)
resetButton.grid(row=3, column=2)
checkmarkLabel.grid(row=4, column=1)


window.mainloop()
