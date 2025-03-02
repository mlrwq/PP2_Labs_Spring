def copy_file(f1, f2):
    with open(f1, "r") as file1:
        cop1 = file1.read()
    with open(f2, "w") as file2:
        file2.write(cop1)

copy_file(r"C:\Users\Admin\OneDrive\Рабочий стол\githowto\repositories\Labs\Lab6\dir-and-files\copy_from.txt", 
          r"C:\Users\Admin\OneDrive\Рабочий стол\githowto\repositories\Labs\Lab6\dir-and-files\insert_to.txt")
