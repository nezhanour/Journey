#get a number from the user
number = int(input("Enter a number: "))
# a variable to store the count of the didgits in the number entered by the user
count = 0
# storing the user's number for printing 
copynumber = number
# a while loop that runs as long as the number is geater than 0
while number != 0:
    number = number // 10
    count = count + 1

print(f"there are {count} digit in the number {copynumber}")