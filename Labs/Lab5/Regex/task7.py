import re

def snake_camel(s):
    spl_str = s.split("_")
    camel = spl_str[0]
    
    for i in spl_str[1:]:
        camel += i[0].upper() + i[1:]

    return camel

snake_str = str(input())
camel_str = snake_camel(snake_str)
print(camel_str)
