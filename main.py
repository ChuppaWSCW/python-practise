
play = "yes"
score=0
QUESTION_FORMAT = "{}\nA. {}  B. {} C. {} D. {}" 

# Ask the user their name and save it
username = input("What's your name?") 

# Greet the user and introduce the quiz
print("Welcome user to the quiz", username)
tries = int(input("How many attempts do you want at each question? 1-4"))
tries = int(tries) 


while play == "yes":
    question_attempts = tries
    while question_attempts > 0:
        # Ask the user a question
        answer = input("What is the color of the ocean").upper()
        if answer == "Blue".upper():
            print("Correct!")
            score=(score+2)
            break
        elif answer == "":
            print("You skipped")
        else:
            print("Wrong!")
        print(" The answer is Blue!")
        # Tell them the correct answer
        print("It is blue")


    # End the quiz
    print("Thank you for playing")
    print("Well done {}. You finished the quiz. Your final score was {}").format(username, score)
    play = input("Do you want to play again?").lower()

print("Goodbye")
