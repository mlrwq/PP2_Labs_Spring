import os

path = input()

if os.path.exists(path):
    print("file exists")
    if os.access(path, os.R_OK):
        print("file is readable")
    if os.access(path, os.W_OK):
        print("file is writable")
    if os.access(path, os.X_OK):
        print("file is executable")
else: 
    print("file doesn't exist")