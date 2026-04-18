easy_questions = [
    {
        "question": "What is 2+2?",
        "options": ["A) 3", "B)4","C)5","D)6"],
        "answer": "B"
    }
]

intermediate_questions = [
    {
        "question": "What is the full form of HTML",
        "options": ["A)Hyper Text MarkUp Language","B)Hyper Text Mockup Language","C)High Mockup Language","D)Hello Top Mock Language"],
        "answer": "A"
    }
]

advance_questions = [
    {
        "question": "What is the full form of HTML",
        "options": ["A)Hyper Text MarkUp Language","B)Hyper Text Mockup Language","C)High Mockup Language","D)Hello Top Mock Language"],
        "answer": "A"
    }
]

print("=============WELCOME TO SMART QUIZ APP=================")

option = True

while option == True:

    print("\nSmart Quiz Application")
    print("\n1: Start the Quiz")
    print("\n2: LeaderBoard")
    print("\n3: Exit")

    choice = int(input("Enter Your Suitable Option: "))

    if choice == 1:

        print("Enter Your Desired Difficulty level")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        difficulty = int(input("Enter Your Choice in Numbers As 1,2,3: "))

        if difficulty == 1:
            selected_questions = easy_questions
        elif difficulty == 2:
            selected_questions = intermediate_questions
        elif difficulty == 3:
            selected_questions = advance_questions

        score = 0

        for q in selected_questions:
            print("\n", q["question"])

            for opt in q["options"]:
                print(opt)

            ans = input("Enter Your Answer: ")

            if ans == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Wrong :( Deducting Score.)")
                score -= 0.25

        print(f"Your Current Score Is {score}")

    elif choice == 3:
        print("Goodbye See You Soon")
        option = False