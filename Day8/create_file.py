#Write all content of a given file into a new file by skipping line number 5

with open('test.txt', 'r') as test:
    lines = test.readlines()
    new = open('new_file.txt', "w")
    counter = 0
    for l in lines:
        if counter == 4 :
            counter  += 1
            continue
        else:
            new.write(l)
        counter +=1
    new.close()
        