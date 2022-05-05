#Exercise 3: Calculate the addition of all numbers from 1 to a given number
#Write a program to accept a number from a user and calculate the addition of all numbers from 1 to a given number

#For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

#using a while loop
#getting user's number
num = int(input("Please enter a number to calculate the addition of all numbers from 1 to your number : "))

i = 1
addition = 0
while i <= num:
    addition = addition + i
    i += 1
print("Sum is: ", addition)


# using for loop
user_number = int(input("Enter a number: ")) 
num_sum = 0
for number in range(user_number + 1):
    num_sum += number
print("the Sum is: ", num_sum)