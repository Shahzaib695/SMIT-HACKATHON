# Questions based on difficulty level
easy_questions = [
    {
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "B"
    },
    {
        "question": "What is the capital of Pakistan?",
        "options": ["A) Lahore", "B) Karachi", "C) Islamabad", "D) Quetta"],
        "answer": "C"
    },
    {
        "question": "What color is the sky on a clear day?",
        "options": ["A) Green", "B) Blue", "C) Red", "D) Yellow"],
        "answer": "B"
    },
    {
        "question": "How many days are in a week?",
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "C"
    },
    {
        "question": "What is 5 - 3?",
        "options": ["A) 1", "B) 2", "C) 3", "D) 4"],
        "answer": "B"
    },
    {
        "question": "What do we use to write?",
        "options": ["A) Spoon", "B) Pen", "C) Plate", "D) Shoes"],
        "answer": "B"
    },
    {
        "question": "How many legs does a cat have?",
        "options": ["A) 2", "B) 3", "C) 4", "D) 5"],
        "answer": "C"
    },
    {
        "question": "What is the color of grass?",
        "options": ["A) Blue", "B) Green", "C) Black", "D) White"],
        "answer": "B"
    },
    {
        "question": "Which is a fruit?",
        "options": ["A) Carrot", "B) Potato", "C) Apple", "D) Onion"],
        "answer": "C"
    },
    {
        "question": "What comes after 9?",
        "options": ["A) 8", "B) 10", "C) 11", "D) 12"],
        "answer": "B"
    }
]
intermediate_questions = [
    {
        "question": "What is 12 x 12?",
        "options": ["A) 144", "B) 121", "C) 132", "D) 150"],
        "answer": "A"
    },
    {
        "question": "Which language is used for web structure?",
        "options": ["A) Python", "B) HTML", "C) C++", "D) Java"],
        "answer": "B"
    },
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which is a programming language?",
        "options": ["A) HTML", "B) CSS", "C) Python", "D) XML"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A) Central Process Unit", "B) Central Processing Unit", "C) Computer Power Unit", "D) Central Program Unit"],
        "answer": "B"
    },
    {
        "question": "What is 50 / 5?",
        "options": ["A) 5", "B) 10", "C) 15", "D) 20"],
        "answer": "B"
    },
    {
        "question": "Which is an input device?",
        "options": ["A) Monitor", "B) Printer", "C) Keyboard", "D) Speaker"],
        "answer": "C"
    },
    {
        "question": "What is H in HTML?",
        "options": ["A) Hyper", "B) High", "C) Home", "D) Help"],
        "answer": "A"
    },
    {
        "question": "Which is used for styling web pages?",
        "options": ["A) HTML", "B) CSS", "C) C", "D) Java"],
        "answer": "B"
    },
    {
        "question": "What is 9 x 9?",
        "options": ["A) 81", "B) 72", "C) 99", "D) 90"],
        "answer": "A"
    }
]
hard_questions = [
    {
        "question": "What is 15^2?",
        "options": ["A) 225", "B) 215", "C) 200", "D) 250"],
        "answer": "A"
    },
    {
        "question": "Which data structure uses LIFO?",
        "options": ["A) Queue", "B) Stack", "C) Array", "D) Tree"],
        "answer": "B"
    },
    {
        "question": "What is binary of 5?",
        "options": ["A) 101", "B) 110", "C) 111", "D) 100"],
        "answer": "A"
    },
    {
        "question": "Which algorithm is fastest for sorting (average)?",
        "options": ["A) Bubble Sort", "B) Merge Sort", "C) Selection Sort", "D) Linear Sort"],
        "answer": "B"
    },
    {
        "question": "What is time complexity of binary search?",
        "options": ["A) O(n)", "B) O(log n)", "C) O(n^2)", "D) O(1)"],
        "answer": "B"
    },
    {
        "question": "Which is not an OOP principle?",
        "options": ["A) Encapsulation", "B) Inheritance", "C) Compilation", "D) Polymorphism"],
        "answer": "C"
    },
    {
        "question": "What does RAM stand for?",
        "options": ["A) Random Access Memory", "B) Read Access Memory", "C) Run Access Memory", "D) Real Active Memory"],
        "answer": "A"
    },
    {
        "question": "Which protocol is used for websites?",
        "options": ["A) FTP", "B) HTTP", "C) SMTP", "D) SSH"],
        "answer": "B"
    },
    {
        "question": "Which is backend language?",
        "options": ["A) HTML", "B) CSS", "C) Python", "D) Bootstrap"],
        "answer": "C"
    },
    {
        "question": "What is 2^5?",
        "options": ["A) 16", "B) 32", "C) 64", "D) 48"],
        "answer": "B"
    }
]
print("=============WELCOME TO SMART QUIZ APP=================")
# starting of program
option = True
leaderboard = [];
while option == True:
    print("\nSmart Quiz Application")
    print("\n1: Start the Quiz")
    print("\n2: LeaderBoard");
    print("\n3: View Last Score");
    print("\n4: Exit");
# choice for menus
    try:
        choice = int(input("Enter Your Suitable Option: "))
    except:
        print("Enter numbers only!");
        continue;
# selection for choice
    if choice == 1:
        name = input("Enter Your Name: \n");
        print("Enter Your Desired Difficulty level");
        print("1. Easy");
        print("2. Medium");
        print("3. Hard");
        # integer validation
        while True:
            try:
                difficulty = int(input("Enter Your Choice in Numbers As 1,2,3: "));

                if difficulty in [1, 2, 3]:
                    break;
                else:
                    print("Choose 1, 2 or 3 only")
            except:
                print("Enter Numbers Only")
        
# question level saver 
        if difficulty == 1:
            selected_questions = easy_questions;
            question_level = "Easy";
        elif difficulty == 2:
            selected_questions = intermediate_questions;
            question_level = "Medium";
        elif difficulty == 3:
            selected_questions = hard_questions;
            question_level = "Hard";
        total_questions = len(selected_questions);
        score = 0
        for q in selected_questions:
            print("\n", q["question"])
            for opt in q["options"]:
                print(opt)
            while True:    
                ans = input("Enter Your Answer (A/B/C/D): ").upper();
                if ans in ["A","B","C","D"]:
                    break;
                else:
                    print("Invalid option! Please enter only A, B, C or D.");
            if ans == q["answer"]:
                print("Correct!")
                score += 1
                print(f"Score = {score}");
            else:
                print(f"Wrong :( The Correct Option Was {q['answer']}");
                score = max(0, score - 1);
        print(f"Your Current Score Is {score}");
        input("Press Enter To Continue");
        percentage = (score * 100) / total_questions
        percentage = round(percentage, 2);
        if percentage < 25:
            level = "Failures";
            print(level);
            print(f"{name} You need to Work On Your Self A Bit Too Much You Ranked As a {level} at {question_level} difficulty.Such a shame");
        elif percentage < 50:
            level = "Beginner";
            print(level);
            print(f"{name} You need to Work On Your Self You Ranked As a {level} at {question_level} difficulty. ");
        elif percentage < 75:
            level = "Intermediate";
            print(level);
            print(f"{name} You Slayed But there is still space for improvement.Still You Ranked As an {level} at {question_level} difficulty. ");
        else:
            level = "Advanced";
            print(level);
            print(f"{name} You did ur best and u ranked as an {level} at {question_level} difficulty. Congratulations ");
        print("Saving Your Record For Leaderboard Purpose :)");
        print("\n===== RESULT =====");
        print("Name:", name);
        print("Score:", score);
        print("Percentage:", percentage);
        print("Level:", level);
        leaderboard.append((name, score, percentage, level));
        last_attempt = (name,score,percentage,level);
    elif choice == 2:
        if len(leaderboard) == 0:
            print("No attempts yet.");
        else:
            print("\n===== LEADERBOARD  =====");
            leaderboard.sort(key=lambda x: x[1],reverse=True);
            i = 1;
            for data in leaderboard:
                print(i, "Name:", data[0], "| Score:", data[1], "| %:", data[2], "| Level:", data[3]);
                i += 1;
    elif choice == 3:
        if last_attempt is None:
            print("No attempts yet.")
        else:
            print("\n===== LAST SCORE =====");
            print("Name:", last_attempt[0]);
            print("Score:", last_attempt[1]);
            print("Percentage:", last_attempt[2]);
            print("Level:", last_attempt[3]);
    elif choice == 4:
        print("Goodbye See You Soon");
        option = False;