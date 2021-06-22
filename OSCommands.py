import os
#a = os.system("date")
path = "C:/Users/Ravi/Desktop/Python/Checking.txt"
#os.mkdir("C:/Users/Ravi/Desktop/Python/c100")


b = os.getcwd()
print (b)

c = os.path.exists(path)
print (c)

d = os.path.splitext("C:/Users/Ravi/Desktop/Python/Checking.txt")
print (d[0])

e = os.listdir()
print (e)