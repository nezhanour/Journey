#Exercise 2: Print the following pattern

#first loop to count from 1 to 5
for i in range(1, 6):
    #second loop to count from 1 to i + 1 : in the first i = 1
    #so second loop will  will go from 1 to i + 1 = 2
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row to separate them
    print('')