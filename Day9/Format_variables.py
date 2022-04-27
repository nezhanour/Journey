#Format variables using a string.format() method.
#Write a program to use string.format() method to format the following three variables as per the expected output
#Given:

totalMoney = 1000
quantity = 3
price = 450
#Expected Output:

#I have 1000 dollars so I can buy 3 football for 450.00 dollars.

txt = "I have {} dollars so I can buy {} football for {:.2f} dollarrs."
print(txt.format(totalMoney, quantity , price))


#User input:
product =  input("What is it that you need? :")
totalmoney = int(input("How much money do you have? : "))
quantity = int(input("How much do you want? : "))
price = float(input("How much the unit cost? : "))

statement = "You have {1} dollars so you can buy {2} {0} for {3:.2f} dollars."
print(statement.format(product, totalmoney, quantity, price))
