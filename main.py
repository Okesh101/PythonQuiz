# Coded by Okesh101

print("Welcome to a Quiz Program.")

print("You are going to have 5 Multiple Choice Questions, which when you've answered, you will see your score.")

score = 0
def question_1():
    print("1. What is the capital of Nigeria?")
    print("A. Lagos")
    print("B. Abuja")
    print("C. Calabar")
    print("D. Port Harcourt")
    answer = input("Your answer: ")
    if answer == "B" or answer == "b":
        return 1
    else:
        return 0
    
def question_2():
    print("2. What year did Nigeria gain independence?")
    print("A. 1999")
    print("B. 1970")
    print("C. 1956")
    print("D. 1960")
    answer = input("Your answer: ")
    if answer == "D" or answer == "d":
        return 1
    else:
        return 0

def question_3():
    print("3. What is the most populated city in Nigeria?")
    print("A. Abuja")
    print("B. Kano")
    print("C. Lagos")
    print("D. Port Harcourt")
    answer = input("Your answer: ")
    if answer == "C" or answer == "c":
        return 1
    else:
        return 0

def question_4():
    print("4. What is the lingua franca of Nigeria?")
    print("A. English")
    print("B. French")
    print("C. Yoruba")
    print("D. Hausa")
    answer = input("Your answer: ")
    if answer == "A" or answer == "a":
        return 1
    else:
        return 0

def question_5():
    print("5. What is the currency of Nigeria?")
    print("A. Naira")
    print("B. Dollar")
    print("C. Euro")
    print("D. Pound")
    answer = input("Your answer: ")
    if answer == "A" or answer == "a":
        return 1
    else:
        return 0

score = question_1() + question_2() + question_3() + question_4() + question_5()
print("You scored: " + str(score) + "/5")
print("Thank you for taking the quiz!")
