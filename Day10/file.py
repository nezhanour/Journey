# Check file is empty or not


### the os method
from asyncore import file_dispatcher
import os 

#getting the size of file.txt
status = os.stat("file.txt").st_size

#checking the size of file.txt
if status == 0:
    print("Empty file")
else:
    print("Not an empty file")

### the path method
from pathlib import Path
xfile = Path("file.txt").stat().st_size
if xfile == 0:
    print("Empty file")
else:
    print("File contain something")
