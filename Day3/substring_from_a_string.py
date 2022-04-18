#Write a program to find how many times substring “Emma” appears in the given string.
def check_word():
    #given string 
    str_x = input("Please enter a statment : ")
    #the word to check how many times it was repeated
    supstring = input("Please enter the word a check : ")
    #counting how many times the word was repeated
    word = str_x.count(supstring)


    print(f"{supstring} appeard {word} times")

check_word()