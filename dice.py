import random
for i in range(100):
    dice = random.randint(1, 6)
    if dice != 6:
        print("your dice number is: ", dice)
        break
    else:
        print("you've got a 6 let's see 2nd chance")    

    