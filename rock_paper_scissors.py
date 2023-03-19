import random
user_score = 0
computer_score = 0

while user_score != 3 and computer_score != 3:

    x = random.randint(1, 3)
    if x == 1 :
        computer_choice = "sang"

    elif x == 2 :
        computer_choice = "kaqaz"

    elif x == 3 :
        computer_choice = "qeichi"

    user_choice = input("sang kaqaz qeichi ?") 


    
    if computer_choice == "sang" and user_choice == "sang":
        user_score = user_score
    elif computer_choice == "sang" and user_choice == "kaqaz":
        user_score = user_score + 1

    elif computer_choice == "sang" and user_choice == "qeichi":
        computer_score = computer_score + 1

    elif computer_choice == "qeichi" and user_choice == "sang":
        user_score = user_score + 1

    elif computer_choice == "qeichi" and user_choice == "kaqaz":
        computer_score = computer_score + 1

    elif computer_choice == "qeichi" and user_choice == "qeichi":
        computer_score = computer_score

    elif computer_choice == "kaqaz" and user_choice == "sang":
        computer_score = computer_score + 1

    elif computer_choice == "kaqaz" and user_choice == "kaqaz":
        computer_score = computer_score

    elif computer_choice == "kaqaz" and user_choice == "qeichi":
        user_score = user_score + 1
    
    print(user_choice)
    print(computer_choice)
    print("user_score is: ", user_score)   
    print("computer score is: ", computer_score) 
if computer_score == 3:
    print("computer wins")

elif user_score == 3:
    print("user wins")