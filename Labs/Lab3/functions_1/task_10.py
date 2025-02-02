def unique(list):
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)

my_list = []
n = int(input())
for i in range (n):
    x = int(input())
    my_list.append(x)

unique(my_list)