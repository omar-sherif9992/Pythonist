from tkinter import *
import math
window=Tk()
window.title("Miles to Kilometers converter")
window.minsize(width=300,height=100)
window.config(background="white",padx=20,pady=20)

# empty=Label(text="")
# empty.grid(row=0,column=0)

input=Entry(width=7)
input.grid(row=0,column=2)

miles=Label(text="Miles",background="white")
miles.grid(row=0,column=3)



output_label=Label(text="0",background="white")
output_label.grid(row=1,column=2)

isequal=Label(text="is equal to",background="white")
isequal.grid(row=1,column=0)

Km=Label(text="Km",background="white")
Km.grid(row=1,column=3)

def calculate():
    output_label["text"]=round((float(input.get())*1.609))

button=Button(text="Calculate",command=calculate,background="white",foreground="black")
button.grid(row=3,column=2)




window.mainloop()