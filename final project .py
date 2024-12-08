#python quiz game
questions = (
    "What is Python?",
    "Which keyword is used to define a function in Python?",
    "What is the correct file extension for Python?",
    "Write an example of a high-level language?",
    "How do you add an item to a list in Python?",
    "How do you start a loop in Python?",
    "How do you create a dictionary in Python?",
    "Which operator is used to compare two values in Python?",
    "Which of the following is used to import a module in Python?",
    "How do you create a list in Python?",
    "How do you insert a comment in Python?",
    "Which of the following is not a Python data type?",
    "Which operator is used to multiply numbers in Python?",
    "Which statement is used to stop a loop?",
    "Which function is used to check the data type of a variable in Python?"
)

options = [
    ("A. A high-level programming language", "B. A snake species", "C. A type of computer hardware", "D. A text editor"),
    ("A. fun", "B. def", "C. func", "D. create"),
    ("A. .py", "B. .ppt", "C. .docx", "D. .txt"),
    ("A. Python, Java", "B. Machine language", "C. Assembly language", "D. All of the above"),
    ("A. add()", "B. append()", "C. insert()", "D. extend()"),
    ("A. loop:", "B. loop()", "C. foreach", "D. for"),
    ("A. <>", "B. []", "C. {}", "D. ()"),
    ("A. =+", "B. <=", "C. =>", "D. =="),
    ("A. include", "B. using", "C. import", "D. require"),
    ("A. ()", "B. {}", "C. <>", "D. []"),
    ("A. @comment", "B. **comment", "C. +comment", "D. #comment"),
    ("A. float", "B. list", "C. map", "D. tuple"),
    ("A. #", "B. %", "C. *", "D. //"),
    ("A. stop", "B. break", "C. exit", "D. return"),
    ("A. datatype:", "B. datatype()", "C. type()", "D. typeof()")
]

answers = ("A", "B", "A", "A", "B", "D", "C", "D", "C", "D", "D", "C", "C", "B", "C")
guesses = []
score = 0
question_num = 0

print("Welcome to Python Quiz Game! It's time to test your Python skills!")
for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"The correct answer is: {answers[question_num]}")

    question_num += 1

print("---------------------")
print("RESULTS")
print("---------------------")

print("Answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score_percentage = int((score / len(questions)) * 100)
print(f"Your score is: {score_percentage}%")
print("Nice try, keep it up!")



