import tkinter
from tkinter import *
from time import sleep
import math

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
time =None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    window.after_cancel(time)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps % 2 == 0:
        timer.config(text="Work", fg=GREEN)
        countdown(WORK_MIN, 0)
    elif reps % 2 == 1 and reps < 7:
        timer.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_MIN, 0)
    else:
        timer.config(text="Loong Break", fg=RED)
        countdown(LONG_BREAK_MIN, 0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(mins, sec):
    global reps
    global time
    if sec > 0:
        if mins >= 10 and sec >= 10:
            canvas.itemconfig(timer_text, text=f"{mins}:{sec}")
        elif mins < 10 and sec < 10:
            canvas.itemconfig(timer_text, text=f"0{mins}:0{sec}")
        elif mins < 10:
            canvas.itemconfig(timer_text, text=f"0{mins}:{sec}")
        elif sec < 10:
            canvas.itemconfig(timer_text, text=f"{mins}:0{sec}")
        time= window.after(1000, countdown, mins, sec - 1)
    elif mins > 0:
        if mins >= 10 and sec >= 10:
            canvas.itemconfig(timer_text, text=f"{mins}:{sec}")
        elif mins < 10 and sec < 10:
            canvas.itemconfig(timer_text, text=f"0{mins}:0{sec}")
        elif mins < 10:
            canvas.itemconfig(timer_text, text=f"0{mins}:{sec}")
        elif sec < 10:
            canvas.itemconfig(timer_text, text=f"{mins}:0{sec}")
        time=window.after(1000, countdown, mins - 1, 59)
    else:
        canvas.itemconfig(timer_text, text="00:00")
        reps += 1
        i = reps
        txt = ""
        while i > 0:
            if i % 2 == 0:
                txt += "✔"
            i -= 1
        checkmark.config(text=txt)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomadoro App")

w = int(window.winfo_screenwidth())
y = int(window.winfo_screenheight())
window.minsize(width=(math.floor(w // 4.5)), height=(math.floor(y / 2.5)))
window.maxsize(width=(math.floor(w // 4.5)), height=((math.floor(y / 2.5))))
window.config(background=YELLOW, padx=50, pady=40)

checkmark = Label(fg=GREEN, background=YELLOW, font=("Helvet", 14, "normal"), highlightthickness=0)
checkmark.grid(row=2, column=1)

timer = Label(text="Timer", fg=GREEN, background=YELLOW, highlightthickness=0, font=("Helvet", w // 40, "bold"))
timer.grid(row=0, column=1)

canvas = Canvas(width=205, height=226)
tomato = PhotoImage(file="/home/omar/PycharmProjects/Python-Project/Projects/Tkinter-apps/Pomadora-App/tomato.png")
canvas.create_image(103, 112, image=tomato)
canvas.config(background=YELLOW, border=0, bd=0, highlightthickness=0, highlightbackground="white")
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=("Helvet", w // 60, "bold"))
canvas.grid(row=1, column=1)

start = Button(command=start_timer, text="start", background="white", font=("Helvet", w // 173, "normal"),
               highlightthickness=0)
start.grid(row=2, column=0)
Reset = Button(command=reset_timer, text="Reset", background="white", font=("Helvet", w // 173, "normal"),
               highlightthickness=0)
Reset.grid(row=2, column=2)

window.mainloop()
