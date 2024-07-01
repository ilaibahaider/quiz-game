questions = ("What is the capital of France?: ",
        "Which planet is known as the Red Planet?: ",
        "What is the largest mammal in the world?: ",
        "How many bones are in the human body?: ",
        "Who wrote Romeo and Juliet?: ")

options = (("A. Berlin", "B. Madrid", "C. Paris", "D. Rome"),
    ("A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"),
    ("A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Great White Shark"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Charles Dickens", "B. J.K rowling", "C. William Shakespeare", "D. Mark Twaine"))

answers = ("C", "B", "B", "A", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
     print("----------------------")
     print(question)
     for option in options[question_num]:
          print(option)

     guess = input("Enter (A, B, C, D): ").upper()
     guesses.append(guess)
     if guess == answers[question_num]:
          score += 1
          print("CORRECT!")
     else:
          print("INCORRECT!")
          print(f"{answers[question_num]} is the correct answer")
     question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
     print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
     print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"your score is: {score} %")
