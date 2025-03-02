def A_Z_files():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in letters:
        file_ns = f"{i}.txt"
        with open(file_ns, "w") as file:
            file.write(f"this is file {file_ns}")

A_Z_files()