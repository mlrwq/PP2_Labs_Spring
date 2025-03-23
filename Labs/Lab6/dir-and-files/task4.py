file_name = input()

with open(file_name, 'r') as file:
    count = sum(1 for i in file)

print(count)