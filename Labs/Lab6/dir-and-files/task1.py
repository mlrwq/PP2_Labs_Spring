import os

def list_dir(path):
    if not os.path.exists(path):
        print("path doesn't exist")
        return
    dir = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) ]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) ]
    all_items = os.listdir(path)

    print(dir)
    print(files)
    print(all_items)
    return

path = input()
list_dir(path)