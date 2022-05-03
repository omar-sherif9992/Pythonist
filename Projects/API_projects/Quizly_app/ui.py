import math,emojis
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
from tkinter import *

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz_brain=quiz_brain
        window = Tk()
        window.title("Quizzler App")
        w = int(window.winfo_screenwidth())
        y = int(window.winfo_screenheight())
        window.minsize(width=(math.floor(w // 1.55)), height=(math.floor(y / 1.25)))
        window.maxsize(width=(math.floor(w // 1.55)), height=((math.floor(y / 1.25))))
        window.config(background=THEME_COLOR, padx=80, pady=90)
        self.window=window
        self.score=Label(bg="white",text="Score : 0",font=("New Roman",20,"italic"))
        self.score.grid(row=0,column=2)
        self.canvas = Canvas(bg="white",width=800, height=500)
        # IMPORTANT: PhotoImage objects should not be created inside a function. Otherwise, it will not work.THEME_COLOR

        self.canvas.config(background="white" ,highlightthickness=0)

        self.question = self.canvas.create_text(400, 200,width=700,text="Word", fill="black", font=("Helvet", w // 60, "bold"))
        self.canvas.grid(row=1, column=1,pady=40)

        self.right_image = PhotoImage(file="images/true.png")
        self.right_button = Button( command=self.correct_ans,image=self.right_image, width=100, height=97, highlightthickness=0)
        self.right_button.grid(row=4, column=2)

        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(command=self.wrong_ans,image=self.wrong_image, width=100, height=97, highlightthickness=0)
        self.wrong_button.grid(row=4, column=0)
        self.get_next_qustion()
        self.window.mainloop()


    def get_next_qustion(self):
        q_text=self.quiz_brain.next_question()
        self.canvas.itemconfig(self.question,text=q_text)

    def white_again(self):
        self.canvas.config(background="white")
        self.get_next_qustion()

    def correct_ans(self):
        if self.quiz_brain.still_has_questions():
            answer=self.quiz_brain.check_answer("true")
            self.score.config(text=f"Score : {self.quiz_brain.score}")
            if not answer:
                self.canvas.config(background="red")
                self.window.after(500, self.white_again)
            else:
                self.canvas.config(background="green")
                self.window.after(500, self.white_again)

        else:
            self.canvas.itemconfig(self.question,text=f"    The End \n\n Your Score : {self.quiz_brain.score}")

    def wrong_ans(self):
        if self.quiz_brain.still_has_questions():
            answer=self.quiz_brain.check_answer("false")
            self.score.config(text=f"Score : {self.quiz_brain.score}")
            if not answer:
                self.canvas.config(background="red")
                self.window.after(1000, self.white_again)
            else:
                self.canvas.config(background="green")
                self.window.after(1000, self.white_again)
        else:
            self.canvas.itemconfig(self.question, text=f"    The End\n\n Your Score : {self.quiz_brain.score}")
