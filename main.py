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

def get_random_questons(questions, num_questions):
    if num_questions > len(questions):
        num_questions = len(questions)

    random_questions = random.sample(questions, num_questions)
    return random_questions


questions = load_questions()
random_queestions = get_random_questons(questions, 1)
print(random_queestions)