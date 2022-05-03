import os
import random

from logo import logo

def choose_Difficulty(i):
    """The player gets to choose the Difficulty level"""
    if "Hard" == str(input("choose your Difficulty 'Hard' or 'Easy'")):
        i = 5
        print("You have 5 attempts")
    else:
        i = 10
        print("you have 10 attempts")
    return i


def play_game():
    print(logo)
    print("Welcome to the guessing Game")
    i=0
    i = choose_Difficulty(i)
    answer=random.randint(0,100)
    while i>0:
        num=int(input("Guess the number: ") )
        if answer<num:
            print("Too High")
        elif answer>num:
            print("Too low")
        else:
            print(f"You got it! The answer was {answer} ")
            break
        i-=1
        print(f"Turns remaining {i}")
    if i==0:
        print(f"You've losed! The answer was {answer}")

play_game()
while str(input("Do you want to play again? 'Yes' or 'No'")) =="Yes":
    play_game()




