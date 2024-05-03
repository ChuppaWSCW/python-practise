# Ask the user their name and save it
username = input("What's your name?") 

# Greet the user and introduce the quiz
print("Welcome user to the quiz", username)

# Ask the user a question
answer = input("What is the color of the ocean")
if answer == "Blue":
    print("You are correct!")
else:
    print("Your Wrong")
# Tell them the correct answer
print("It is blue")

# End the quiz
print("Thank you for playing")

