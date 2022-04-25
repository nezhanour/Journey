#Convert Decimal number to octal using print() output formatting
#Given:
# num = 8
# Expected Output:
# The octal number of decimal number 8 is 10


num = int(input("Please enter a number to convert to octal: "))

print("The octal number of decimal number ", num ,"is", "%o" % num )
