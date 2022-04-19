#Create a new list from a two list using the following condition
#Given a two list of numbers, 
# write a program to create a new list such that the new list should contain odd numbers from the first list 
# and even numbers from the second list.

#list1 = [10, 20, 25, 30, 35]
#list2 = [40, 45, 60, 75, 90]
#list3 =

def two_lists():
    list1 = input("Please enter some numbers: ")
    list2 = input("Please enter some numbers: ")
    result = []
    list1 = list1.split(' ') 
    list2 = list2.split(' ') 

    

    for item in range(len(list1)):
        list1[item] = int(list1[item])
        if list1[item] % 2 != 0:
            result .append(list1[item])

    for item in range(len(list2)):
        list2[item] = int(list2[item])
        if list2[item] % 2 == 0:
            result .append(list2[item])
    
    return result 

print("result list: ", two_lists())