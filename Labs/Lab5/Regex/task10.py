import re

def camel_snake(s):
    snake = re.sub(r"([a-z])([A-Z])", r"\1_\2" , s)
    return snake.lower()

str = str(input())
print(camel_snake(str))