import os

f = input()

if os.path.exists(f):
    print("Checked")
else:
    print("error")

fname,directory = os.path.split(f)
print(f"fname: {fname}")
print(f"directory: {directory}")