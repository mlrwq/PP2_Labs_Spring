class stringprocess():
    def __init__(self):
        self.s = ""
    
    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())

my_string = stringprocess()
my_string.get_string()
my_string.print_string()