my_list = []
n = int(input())

for i in range(n):
    x = str(input())
    my_list.append(x)

file_n = input()

with open(file_n, "w") as file:
    for i in my_list:
        file.write(i + " ")