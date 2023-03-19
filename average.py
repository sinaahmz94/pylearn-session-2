sum_of_scores = 0
i = 0
while input("type exit to stop otherwise press enter") != "exit" :
    score = float(input("please enter your scores: "))
    i = i + 1
    sum_of_scores = sum_of_scores + score

average = sum_of_scores / i
print("your average is: ", average)
