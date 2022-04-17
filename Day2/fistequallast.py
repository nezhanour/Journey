# Write a function to return True if the first and last number of a 
# given list is same. If numbers are different then return False.

def is_equal(numbers):
    if numbers[0] == numbers[-1]:
        return True
    return False


numbers = [10, 20, 30, 40, 10]
print(is_equal(numbers)) 
numbers_y = [75, 65, 35, 75, 30]
print("the result is " , is_equal(numbers_y)) 