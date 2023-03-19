h = int(input("please enter hours: "))
m = int(input("please enter minutes: "))
s = int(input("please enter seconds: "))
h_to_s = h * 3600
m_to_s = m * 60
total = h_to_s + m_to_s + s
print("total seconds are: ", total)