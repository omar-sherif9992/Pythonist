import random
from Hangman_Logo import logo
from Hangman_words import wordList
from Hangman_drawing import stages

print(logo)

choosenWord = random.choice(wordList)

wrongCounter = 0
correctCounter = 0
finalWord = []
stageCounter = 6

for letter in choosenWord:
    finalWord += ["_   "]

gameFlag = False
flag = False
dubFlag = False
while True:
    if dubFlag:
        print("it's already written ")
        guess = input("Guess another letter: ").lower()
    else:
        guess = input("Guess letter: ").lower()
    dubFlag = False
    i = 0
    flag = False
    for letter in choosenWord:
        if letter == guess and finalWord[i] == (letter + "   "):
            dubFlag = True
            break
        if letter == guess and finalWord[i] != (letter + "   "):
            finalWord[i] = letter + "   "
            flag = True
            correctCounter += 1
        i += 1

    if flag == False and dubFlag == False:
        stageCounter -= 1
        print(f"wrong answer!! \n  {''.join(finalWord)}   {stages[stageCounter]}")

    else:
        print(f"correct answer!! \n   {''.join(finalWord)} {stages[stageCounter]}")
    if correctCounter == len(choosenWord):
        gameFlag = True
        break
    if stageCounter == 0:
        gameFlag = False
        break

if gameFlag:
    print("You won the game!!")
else:
    print("You've loss the game!!")
