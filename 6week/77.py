import shutil

a = shutil.copy("input.txt","input2.txt")
aa = open("input2.txt","r")
b = aa.read()
print(b)