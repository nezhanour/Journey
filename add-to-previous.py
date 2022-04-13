#Write a program to iterate the first 10 numbers and in each 
# iteration, print the sum of the current and previous number.

def add_to_previous():
    previous_num = 0
    for n in range(10):
        print(f"the number {n} added to the previous number {previous_num} is {n + previous_num}")
        previous_num = n
        
print("Printing current and previous number sum in a range(10)")
add_to_previous()