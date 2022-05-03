
import math,requests
from tkinter import *


def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    quote = response.json()
    quote = quote["quote"]
    while len(quote)>60:
        response=requests.get(url="https://api.kanye.rest/")
        quote=response.json()
        quote=quote["quote"]
    canvas.itemconfig(quote_text,text=quote)

    #Write your code here.



window = Tk()
window.title("Kanye Says...")
window.config(padx=90, pady=50,background="white")
w = int(window.winfo_screenwidth())
y = int(window.winfo_screenheight())
window.minsize(width=(math.floor(w // 3.85)), height=(math.floor(y / 1.70)))
window.maxsize(width=(math.floor(w // 3.85)), height=((math.floor(y / 1.70))))
canvas = Canvas(width=300, height=414,background="white",highlightthickness=0,)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote,background="white")
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()