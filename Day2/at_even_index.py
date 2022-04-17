def even_index(word):
    word_length = len(word)
    for n in range(0 , word_length, 2):
        print(word[n]) 


word = input("Please enter a word : ")
print("Original String is " + word)
print("Printing only even index chars")
even_index(word)
#word[n] 
#pynative