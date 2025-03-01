import os

path = input()

if not os.path.exists(path):
    print("no such directory")
else:
    print("file exists")


if not os.access(path, os.R_OK):
    print("file isnt readable ")
else:
    print("file passed check for readability")

if not os.access(path, os.W_OK):
    print("file isnt writable ")
else:
    print("file passed check for writability")
    

if not os.access(path, os.X_OK):
    print("file isnt executable ")
else:
    print("file passed check for executability")