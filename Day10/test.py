# Read line number 4 from the file "test.txt"
with open("test.txt", "r") as f:
    print(f.readlines()[3], end="")
