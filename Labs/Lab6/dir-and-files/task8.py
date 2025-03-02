import os

def delete_by_path(path):
    if os.path.exists(path) and os.access(path, os.R_OK):
        print("path exists and accessible")
        os.remove(path)
        print("file is deleted")
    else:
        print("path doesn't exist")

path = input()
delete_by_path(path) 