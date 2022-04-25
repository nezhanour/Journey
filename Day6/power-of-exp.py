#Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

def exponent(base, exp):
   
    result = 1
    while exp > 0:
        result = result * base
        exp -= 1
    

    print(f"{base} raises to the power of {exp}: ", result)

base = int(input("Please enter a number greater than 0 : "))
exp = int(input("Please enter a number greater than 0 : "))
exponent( base , exp )
