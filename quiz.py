# bank of questions
questions = {
    1: "What is the largest country in the world by area?",
    2: "What river is the longest in the world?",
    3: "Which country has the most natural lakes?",
    4: "What is the smallest country in the world?",
    5: "Which desert is the largest in the world?",
    6: "Which country has the longest coastline?",
    7: "What mountain is the tallest in the world above sea level?",
    8: "What is the capital city of Australia?",
    9: "Which two continents are entirely in the Southern Hemisphere?",
    10: "What is the longest river in Asia?",
    11: "Which country is both a continent and a country?",
    12: "What is the largest island in the world?",
    13: "Which country has the most time zones?",
    14: "What city is known as the City of Canals?",
    15: "Which African country has the largest population?",
    16: "What is the deepest point in the world's oceans?",
    17: "Which river flows through Paris?",
    18: "What is the largest lake in Africa?",
    19: "Which country is known as the Land of the Rising Sun?",
    20: "What is the driest place on Earth?",
}

# bank of correct answers for question bank
correct_answers = {
    1: "Russia",
    2: "Nile",
    3: "Canada",
    4: "Vatican",
    5: "Sahara",
    6: "Canada",
    7: "Everest",
    8: "Canberra",
    9: "Australia and Antarctica",
    10: "Yangtze",
    11: "Australia",
    12: "Greenland",
    13: "France",
    14: "Venice",
    15: "Nigeria",
    16: "Mariana Trench",
    17: "Seine",
    18: "Lake Victoria",
    19: "Japan",
    20: "Atacama",
}

# getting user input
# updating empty dict with answers
responses = {}

for question_num, question in questions.items():
    answer = input(question + " \nEnter answer here: ")
    responses.update({question_num: answer.lower()})

# counting the number of correct answers
total_number_of_answer = len(responses)
correct_answer_counter = 0

# looping through dict of responses from user
for number, answer in responses.items():
    if (answer in correct_answers[number].lower() or
            correct_answers[number].lower() in answer.lower()):
        correct_answer_counter += 1

# print total number of correct answers
print(f"You have {correct_answer_counter} correct answers out of {
      total_number_of_answer} total answers")

print("Here are the correct answers:\n")
for num, answer in correct_answers.items():
    print(f"{num}. {answer}")
