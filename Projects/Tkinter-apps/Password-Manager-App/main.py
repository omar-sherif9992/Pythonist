from tkinter import *
from tkinter import messagebox
import math
import pandas
import random


# ----------------------------  Constants ------------------------------- #
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password.delete(0, END)
    random_password = ""
    flag = True
    list = [4, 1, 2]
    while flag:
        if list[0] == 0 and list[1] == 0 and list[2] == 0:
            break
        list_index = random.randint(0, 2)
        if list_index == 0 and list[0] != 0:
            random_password += str(letters[random.randint(0, len(letters) - 1)])
            list[0] -= 1
        elif list_index == 1 and list[1] != 0:
            random_password += str(symbols[random.randint(0, len(symbols) - 1)])
            list[1] -= 1
        elif list_index == 2 and list[2] != 0:
            random_password += str(numbers[random.randint(0, len(numbers) - 1)])
            list[2] -= 1
    password.insert(0, random_password)
    pyperclip.copy(random_password)


# ---------------------------- delete Entries --------------------------------------- #
def delete_entries():
    website.delete(0, END)
    email.delete(0, END)
    email.insert(0, "omar.sherif9992@gmail.com")
    password.delete(0, END)


# ---------------------------- clear csv --------------------------------------------- #
def clear_data():
    if not messagebox.askyesno(title="Confirmation to clear Data", message="Are You Sure ?"):
        return

    new_dict = {"Website": [], "Email": [], "Password": []}
    df = pandas.DataFrame(new_dict)
    df = df.dropna()
    df.to_csv("data.csv")


# ---------------------------- reading csv ------------------------------- #

def format_csv(new_email, new_password, new_website):
    new_dict={}
    try:
        if not ".Com" in new_website:
            new_website+=".Com"
        data = pandas.read_csv("data.csv")
        emails = data["Email"].tolist()
        passwords = data["Password"].tolist()
        websites = data["Website"].tolist()


        if new_website in websites:
            if  messagebox.askyesno(title="Duplicated Info",
                                       message=f"This website {new_website} was previously added\n do you wish to replace it"):
                index=websites.index(new_website)
                websites = websites[:index] + websites[index + 1:]
                emails = emails[:index] + emails[index + 1:]
                passwords= passwords[:index] + passwords[index + 1:]

            else:
                return

        emails.append(new_email)
        websites.append(new_website)
        passwords.append(new_password)
        new_dict = {"Website": websites, "Email": emails, "Password": passwords}
    except :
        new_dict = {"Website": [new_website], "Email": [new_email], "Password": [new_password]}
    finally:
        df = pandas.DataFrame(new_dict)
        df = df.dropna()
        df.to_csv("data.csv")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_txt = website.get()
    password_txt = password.get()
    email_txt = email.get()
    if website_txt == "":
        messagebox.showinfo(message="please enter the website name", title="Missing info")
        return
    if password_txt == "":
        messagebox.showinfo(message="please enter the Password", title="Missing info")
        return
    if email_txt == "":
        messagebox.showinfo(message="please enter the Email", title="Missing info")
        return
    if (not (".com" in email_txt)) or (not "@" in email_txt):
        messagebox.showinfo(message="please enter correct Email", title="Missing info")
        return
    format_csv(email_txt.title(), password_txt, website_txt.title())
    delete_entries()
# ---------------------------- Search for EMAIL & PASSWORD ------------------------------- #
def search():
    new_website=website.get()
    if new_website == "":
        return

    new_website=new_website.title()
    if not ".Com" in new_website:
        new_website += ".Com"



    try:
        data = pandas.read_csv("data.csv")
        emails = data["Email"].tolist()
        passwords = data["Password"].tolist()
        websites = data["Website"].tolist()
        if not (new_website in websites):
             messagebox.showinfo(title="WARNING", message=f"This website {new_website} is not Found")
             return

        index=websites.index(new_website)
        messagebox.showinfo(title="User Info", message=f"*Website :\n{new_website}\n\n*Email :\n{emails[index]}\n\n *Password :\n{passwords[index]}")
    except :
        messagebox.showinfo(title="WARNING", message=f"This website {new_website} is not Found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator App")

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

website_label = Label(text="Website :")
website_label.config(background="white", border=0, bd=0, highlightthickness=0, highlightbackground="white", padx=20,
                     pady=10)
website_label.grid(row=1, column=0)

website = Entry(width=20)
website.grid(row=1, column=1)
website.focus()
search_password = Button(text="Search", width=30, command=search)
search_password.grid(row=1, column=2)


email_label = Label(text="Email address :", padx=10, pady=10)
email_label.config(background="white", border=0, bd=0, highlightthickness=0, highlightbackground="white")
email_label.grid(row=2, column=0)

email = Entry(width=54)
email.grid(row=2, column=1, columnspan=2)
email.insert(0, "omar.sherif9992@gmail.com")

password_label = Label(text="Password :", padx=10, pady=10)
password_label.config(background="white", border=0, bd=0, highlightthickness=0, highlightbackground="white")
password_label.grid(row=3, column=0)

password = Entry(width=20)
password.grid(row=3, column=1)

generate_password = Button(text="Generate password", width=30, command=password_generator)
generate_password.grid(row=3, column=2)

Add = Button(width=51, text="Add", background="white", command=save_password)
Add.grid(row=4, column=1, columnspan=2)

clear = Button(width=51, text="clear data", background="white", command=clear_data)
clear.grid(row=5, column=1, columnspan=2)

window.mainloop()
