def is_divisible_by_five():
    #getting number from the user 
    numbers = input("Please enter some numbers : ")
    
    #spliting the string from the input function by space 
    listOfnumbers = numbers.split(' ') 

    #sorting the numbers into a list after Converting each element to an integer 
    for num in range(len(listOfnumbers)):
        listOfnumbers[num] = int(listOfnumbers[num])

    print("the given list is : " + str(listOfnumbers))
    
    #checking if the number are divisible by 5
    print("the numbers that are divisible by 5 are :")
    for item in listOfnumbers:
        if item % 5 == 0:
            print(item)

    
is_divisible_by_five()