#Exercise 5: Display numbers from a list using loop
#Write a program to display only those numbers from a list that satisfy the following conditions
#The number must be divisible by five
#If the number is greater than 150, then skip it and move to the next number
#If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    #checking if the number is greater than 500 if yes then the loop stop
    if num > 500:
        break
    #checking if the number is greater than 15O if yes then we skip to the next and move to the next number
    elif num > 150:
        continue
    #checking if the number is divisible by five if yes we print the number
    elif num % 5 == 0:
        print(num)