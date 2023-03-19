n = int(input("please enter how many arrays you want: "))
first_number = 0
second_number = 1
print(first_number)
print(second_number)
for i in range(n-2):
    third_number = first_number + second_number

    print(third_number)
    first_number = second_number
    second_number = third_number
