import os

path = input()

if os.path.exists(path):
    print("file exists")

    dir, fil = os.path.split(path)
    print(dir)
    print(fil)