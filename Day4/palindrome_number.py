#my attempt
number = input("Please enter a number: ")

reversed_number = number[::-1]
if reversed_number == number:
    print('the given number is a Palindrome number')
else:
    print('the given number is not a Palindrome number')


#second attempt based on a solution using while loop i found online u
#def is_palindrome_number():
num = int(input("Please enter a number: "))
user_num = num
revs_num = 0

while num > 0:
    num_remainder = num % 10
    revs_num = revs_num * 10 + num_remainder
    num = num // 10
print(revs_num)

if revs_num == user_num:
    print('the given number is a Palindrome number')
else:
    print('the given number is not a Palindrome number')

#print(is_palindrome_number())