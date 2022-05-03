from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def play_game():
    question_bank = []
    for question in question_data:
        question_bank.append(Question(question["text"], question["answer"]))

    quiz = QuizBrain(question_bank)
    score = 0
    while quiz.still_has_question():
        score = check_answer(quiz, score)

    print(f"Your Final Score is  {score}/{len(question_bank)} ")


def check_answer(quiz, score):
    if quiz.question_list[quiz.question_number].answer == (quiz.next_question()):
        score = score + 1
        print(f"You are Correct !\n Current Score : {score} ")
    else:
        print(f"You are Wrong !\n Current Score : {score} ")
    return score


play_game()
while str(input("Do you want to play again? 'Yes' or 'No'")) == "Yes":
    play_game()
