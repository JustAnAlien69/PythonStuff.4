import os
import shutil

source = "C:/Users/Ravi/Desktop/Python/OSandShutil/text.txt"
destination = "C:/Users/Ravi/Desktop/Python/text1.txt"

shutil.copy(source,destination)

source1 = "C:/Users/Ravi/Desktop/Python/Checking.txt"
destination1 = "C:/Users/Ravi/Desktop/Python/OSandShutil"


shutil.move(source1,destination1)