import os

path = input()

if not os.path.exists(path):
    print("no such directory")
else:
    directory = os.listdir(path)
    files = [f for f in directory if os.path.isfile(os.path.join(path,f))]
    dirs = [f for f in directory if os.path.isfile(os.path.join(path,f))]

print("Files:", files)
print("Directories:", dirs)
print("Path:", directory)