
   
#Given two integer numbers return their product only if the product is 
# greater than 1000, else return their sum.


def calculate(num1, num2):

    if num1 * num2 > 1000:
        return num1 * num2

    else:
        return num1 + num2

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))

print(calculate(num1, num2))