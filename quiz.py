# bank of questions
questions = {
    1: "How many bones are there in the human body?",
    2: "What is the capital of turkey?",
    3: "What is the largest continent?",
}

# bank of correct answers for question bank
correct_answers = {
    1: 206,
    2: "istanbul",
    3: "asia",
}
# getting user input
# updating empty dict with answers
responses = {}

for question_num, question in questions.items():
    answer = input(question + " ")
    responses.update({question_num: answer.lower()})


for question_num, answer in responses.items():
    print(f"{question_num}. {answer.title()}")

# counting the number of correct answers
total_number_of_answer = len(responses)
correct_answer_counter = 0

# looping through dict of responses from user
for number, answer in responses.items():
    if answer == correct_answers[number]:
        correct_answer_counter += 1
        print("correct answer!")
    else:
        print(f"{answer.title()} is not the correct answer")

# print total number of correct answers
print(f"You have {correct_answer_counter} out of {
      total_number_of_answer} correct answers")
