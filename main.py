# Questions will be generated randomly
# json file to strore questions
# loop to continue test
# 
import random
import json


def load_questions():
    with open("questions.json", "r") as f:
        questions = json.load(f)["questions"]

    return questions

questions = load_questions()
print(questions)