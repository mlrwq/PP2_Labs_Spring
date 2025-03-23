def spy_game(nums):
    spy = [0, 0, 7]
    ind = 0
    for i in nums:
        if i == spy[ind]:
            ind += 1
        if ind == len(spy):
            return True
    return False
        

my_list = []
n = int(input())
for i in range (n):
    x = int(input())
    my_list.append(x)

print(spy_game(my_list))