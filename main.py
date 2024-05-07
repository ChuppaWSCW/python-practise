score=0

# Ask the user their name and save it
username = input("What's your name?") 

# Greet the user and introduce the quiz
print("Welcome user to the quiz", username)

# Ask the user a question
answer = input("What is the color of the ocean").upper()
if answer == "Blue".upper():
    print("Correct!")
    score=(score+2)
elif answer == "":
    print("You skipped")
else:
    print("Wrong!")
print(" The answer is Blue!")
# Tell them the correct answer
print("It is blue")

# End the quiz
print("Thank you for playing")



print("Your Score is",score)
