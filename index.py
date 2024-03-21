print("Hello there! Welcome to basic programming quiz game.")

play = input("Do you want to play?(yes/no): ")
if play.lower() != 'yes':
    print("Quiting the game! Bye!")
    quit()
else:
     print("Okay, let's play!(Each question has a total of 2 points)")

score = 0
question = input("What does HTML stand for? ")
if question.lower() == "hypertext markup language":
     print("Correct!")
     score += 2
else:
     print("Incorrect!")

question = input("What does CSS stand for? ")
if question.lower() == "cascading style sheets":
     print("Correct!")
     score += 2
else:
     print("Incorrect!")

question = input("Which programming language is known for its use in web development and creating dynamic web pages? ")
if question.lower() == "javascript":
     print("Correct!")
     score += 2
else:
     print("Incorrect!")

question = input("What does HTTP stand for? ")
if question.lower() == "hypertext transfer protocol":
     print("Correct!")
     score += 2
else:
     print("Incorrect!")

print("You score is " + str(score))
print("You got " + str((score/8)*100) + " %")

