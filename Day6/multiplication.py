#Accept numbers from a user
#Write a program to accept two numbers from the user and calculate multiplication

def multiplication(num1, num2):
    print(f"the result of multiplication of number {num1}  and numbre {num2}  is : ", num1 * num2)

multiplication(num1=int(input("Please enter a numbre: ")), num2=int(input("Please enetr a second number: ")))
