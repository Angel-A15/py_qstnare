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

def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(str(i + 1) + ".", option)

    number = int(input("Select the correct number:"))
    if number < 1 or number > len(question["options"]):
        print("Invalid choice, defaulting to wrong answer.")
        return False
    correct = question["options"][number - 1] == question["answer"]
    return correct

questions = load_questions()
total_questions = int(input("Enter the number of questions:"))
random_queestions = get_random_questons(questions, total_questions)
correct = 0

for question in random_queestions:
    is_correct = ask_question(question)
    if is_correct:
        correct += 1
    print("------------------")

print("Summary")
print("Total Questions:", total_questions)
print("Correct Answers:", correct)
print("Score:", str(round((correct / total_questions) * 100, 2)) + "%")