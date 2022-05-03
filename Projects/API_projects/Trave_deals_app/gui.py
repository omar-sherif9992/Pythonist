from tkinter import *
from tkinter import messagebox
import math
from email_manager import EmailManager
import main


class Gui:

    # ---------------------------- UI SETUP ------------------------------- #
    def __init__(self):
        self.email_manager = EmailManager()
        window = Tk()
        window.title("Travel club App")
        w = int(window.winfo_screenwidth())
        y = int(window.winfo_screenheight())
        window.minsize(width=(math.floor(w // 2.25)), height=(math.floor(y / 2.05)))
        window.maxsize(width=(math.floor(w // 2.25)), height=((math.floor(y / 2.05))))
        window.config(background="white", padx=50, pady=40)

        canvas = Canvas(width=600, height=260)
        lock = PhotoImage(file="logo.png")
        canvas.create_image(300, 130, image=lock)
        canvas.config(background="white", border=0, bd=0, highlightthickness=0, highlightbackground="white")
        canvas.grid(row=0, column=1, columnspan=3)

        first_name_label = Label(text="First name :")
        first_name_label.config(background="white", border=0, bd=0, highlightthickness=0, highlightbackground="white",
                                padx=20,
                                pady=10)
        first_name_label.grid(row=1, column=0)

        self.first_name = Entry(width=54)
        self.first_name.grid(row=1, column=1)
        self.first_name.focus()

        self.last_name_label = Label(text="Last name :", padx=10, pady=10)
        self.last_name_label.config(background="white", border=0, bd=0, highlightthickness=0,
                                    highlightbackground="white")
        self.last_name_label.grid(row=2, column=0)
        self.last_name = Entry(width=54)
        self.last_name.grid(row=2, column=1)

        email_label = Label(text="Email :", padx=10, pady=10)
        email_label.config(background="white", border=0, bd=0, highlightthickness=0, highlightbackground="white")
        email_label.grid(row=3, column=0)

        self.email = Entry(width=54)
        self.email.grid(row=3, column=1)
        Add = Button(width=54, text="Add", background="white", command=self.save_data)
        Add.grid(row=4, column=1)

        self.update = Button(width=54, text="check deals", background="white", command=main.flights)
        self.update.grid(row=5, column=1)
        window.mainloop()

    # ---------------------------- delete Entries --------------------------------------- #
    def delete_entries(self):
        self.first_name.delete(0, END)
        self.email.delete(0, END)
        self.last_name.delete(0, END)

    # ---------------------------- SAVE PASSWORD ------------------------------- #
    def save_data(self):
        first_name_txt = self.first_name.get()
        self.last_name_txt = self.last_name.get()
        self.email_txt = self.email.get()
        if first_name_txt == "":
            messagebox.showinfo(message="please enter the First name", title="Missing info")
            return
        if self.last_name_txt == "":
            messagebox.showinfo(message="please enter the Last name", title="Missing info")
            return
        if self.email_txt == "":
            messagebox.showinfo(message="please enter the email", title="Missing info")
            return
        if (not (".com" in self.email_txt)) or (not "@" in self.email_txt):
            messagebox.showinfo(message="please enter correct email", title="Missing info")
            return
        check = self.email_manager.add_email(first_name=first_name_txt, last_name=self.last_name_txt,
                                             email=self.email_txt)
        if check:
            messagebox.showinfo(message="You've joined the club", title="Congratulations")
        else:
            messagebox.showinfo(message="You're already the club", title="Duplicated Info")

        self.delete_entries()


Gui()
