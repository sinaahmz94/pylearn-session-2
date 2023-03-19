a = int(input("please enter the number"))
hours = a // 3600
minutes = (a - (hours * 3600)) // 60   
seconds = (a - (hours * 3600) - (minutes * 60))
print(hours," hrs:", minutes," min:", seconds, "sec")