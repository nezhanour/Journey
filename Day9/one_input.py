#Accept any three string from one input() call
#Write a program to take three names as input from a user in the single input() function call.


name1 , name2, name3 = input("Enter three names: ").split()
print("Name 1 =",name1.capitalize(),"\nName 2 =",name2.capitalize(),"\nName 3 =",name3.capitalize())