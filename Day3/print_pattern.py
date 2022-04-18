
#My solution 
#it's my lazy solution 
for num in range(6):
    num = str(num)*num
    print(num) 


#the site solution
for num in range(6):
    for i in range(num):
        print(num, end=' ')
    print("\n")