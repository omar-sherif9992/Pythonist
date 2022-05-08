from tkinter import *
from tkinter import messagebox
import math
from function import stringToFunction
import matplotlib.pyplot as plt
import numpy as np


# ---------------------------- Generate Graph ------------------------------- #

def generateGrapgh():
    ''' Generates the Graph'''
    min = float(min_x.get())
    max = float(max_x.get())
    try:
        if min == "":
            messagebox.showinfo(message="please enter the Minimum Value of X", title="Missing info")
            return
        if max == "":
            messagebox.showinfo(message="please enter the Maximum Value of X", title="Missing info")
            return
        min = float(min)
        max = float(max)
        if (min > max):
            messagebox.showinfo(message="please Min have to be less than Max", title="Wrong Input")
            return
        func = function.get()

        if func == "":
            messagebox.showinfo(message="please enter the Function f(x)", title="Missing info")
            return
        func = stringToFunction(func)
        x = np.linspace(min, max, 250)
        plt.plot(x, func(x))
        plt.xlim(min, max)
        plt.show()
    except ValueError as error_message:
        messagebox.showinfo(message=error_message, title="Wrong Input")
        return
    except:
        messagebox.showinfo(message="Erorr Occurred Please Check Your Inputs", title="Wrong Input")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Function Generator App")

w = int(window.winfo_screenwidth())
y = int(window.winfo_screenheight())
window.minsize(width=(math.floor(w // 2.85)), height=(math.floor(y / 2.25)))
window.maxsize(width=(math.floor(w // 2.85)), height=((math.floor(y / 2.25))))
window.config(background="white", padx=50, pady=40)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(50, 100, image=lock)
canvas.config(background="white", border=0, bd=0, highlightthickness=0, highlightbackground="white")
canvas.grid(row=0, column=1, columnspan=2)

# ================ f(x) ==========#

function_label = Label(text="Function f(x) :", padx=10, pady=10)
function_label.config(background="white", border=0, bd=0, highlightthickness=0, highlightbackground="white")
function_label.grid(row=1, column=0)

function = Entry(width=54)
function.grid(row=1, column=1, columnspan=2)
function.focus()

# ================ Min X ==========#
min_x_label = Label(text="Min x :")
min_x_label.config(background="white", border=0, bd=0, highlightthickness=0, highlightbackground="white", padx=20,
                   pady=10)
min_x_label.grid(row=2, column=0)

min_x = Entry(width=54)
min_x.grid(row=2, column=1, columnspan=2)

# ================ Max X ==========#
max_x_label = Label(text="Max x :")
max_x_label.config(background="white", border=0, bd=0, highlightthickness=0, highlightbackground="white", padx=20,
                   pady=10)
max_x_label.grid(row=3, column=0)

max_x = Entry(width=54)
max_x.grid(row=3, column=1, columnspan=2)

generate_button = Button(width=51, text="Generate Graph", background="white", command=generateGrapgh)
generate_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
