[]
list1 = [10, 20, 30, 40, 50]

rev = reversed(list1)
for item in rev:
    print(item)

print("@@@@@@@@@@@@@@@@@")
lenght = len(list1) - 1
for number in range(lenght, -1, -1):
    print(list1[number])