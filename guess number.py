import random

computer_number = random.randint(10, 40)
for i in range(10):
    user_number = int(input("please enter your number: "))

    if computer_number == user_number:
        print("mashalla👌")
        print("your attempts to the correct answer: ", i+1,)
        break
    elif computer_number > user_number:
        print("go up") 

    elif computer_number < user_number:
        print("go down")