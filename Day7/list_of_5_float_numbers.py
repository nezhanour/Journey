#Accept a list of 5 float numbers as an input from the user
#Expected Output:
#[78.6, 78.6, 85.3, 1.2, 3.5]
#78.6 78.6 85.3 1.2 3.5

numbers = []

for item in range(1,6):
    print('Number', item, ':', end=" ")
    float_number = float(input("Enter number : "))
    numbers.append(float_number)

print("User list is : ", numbers)


