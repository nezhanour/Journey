#Create a new list from a two list using the following condition
#Given a two list of numbers, 
# write a program to create a new list such that the new list should contain odd numbers from the first list 
# and even numbers from the second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []

def two_lists():
    list1
    for item in list1:
        if item % 2 != 0:
            list3.append(item)

    for item in list2:
        if item % 2 == 0:
            list3.append(item)
    
    return list3


print(two_lists())