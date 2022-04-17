#Write a program to remove characters from a string starting/
#  from zero up to n and return a new string.

def remove_chars(txt, position):
    new_txt = txt[position :]
    return new_txt


txt = input("Please give a word : ")
position = int(input("Please give a number "))
print("the word you chose is " +  txt )

new_word = remove_chars(txt, position)
print(f"the new word after removing {position} characters is {new_word}.")
