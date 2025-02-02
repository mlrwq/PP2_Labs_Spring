def has_33(nums):
    for i in range (len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False 
    

my_list = []
n = int(input())
for i in range (n):
    x = int(input())
    my_list.append(x)

print(has_33(my_list))