from logo import logo
from logo import vs
from data import data
import random



def play_game():
    print(logo)
    print("Welcome to Higher-Lower Game")
    score = 0
    while True:
        index1 = random.randint(0, len(data) - 1)
        index2 = random.randint(0, len(data) - 1)
        while index2 == index1:
            index2 = random.randint(0, len(data) - 1)
        print(f"Compare A: {data[index1]['name']} , a {data[index1]['description']} from {data[index1]['country']} ")
        print(vs)
        print(f"Compare B: {data[index2]['name']} , a {data[index2]['description']} from {data[index2]['country']} ")
        choose = str(input("Who has more followers? 'A' or 'B'"))
        if choose == 'A' and data[index1]['follower_count'] > data[index2]['follower_count']:
            score += 1
            print("You are correct!!")
            print(f"Your Score {score}")
        elif choose == 'B' and data[index1]['follower_count'] < data[index2]['follower_count']:
            score += 1
            print("You are correct!!")
            print(f"Your Score {score}")
        else:
            print("You've losed the Game")
            print(f"Your Score {score}")
            break


play_game()
while str(input("Do you want to play again? 'Yes' or 'No'")) == "Yes":
    play_game()
