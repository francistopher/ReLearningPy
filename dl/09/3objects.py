print("# The __init__ function may have as many arguments for your disposal. But once it's")
print("# instantiated and we have an object, these 'functions' are called methods")

print("""
class complex_number(): # Featured in a previous version of the Pre-Calc Math Engine
    def __init__(self, real_number, imaginary_number):
        self.real_number = real_number
        self.imaginary_number = imaginary_number

    def get_string(self):
        return str(self.real_number) + " + " + str(self.imaginary_number) + "i"

number = complex_number(2, 3)
output = number.get_string() # calling get_string method

print(output) # output below
""")


class complex_number():
    def __init__(self, real_number, imaginary_number):
        self.real_number = real_number
        self.imaginary_number = imaginary_number

    def get_string(self):
        return str(self.real_number) + " + " + str(self.imaginary_number) + "i"

number = complex_number(2, 3)
output = number.get_string()

print(output)

print("\n# You can store your methods for later")

print("""
number_string = number.get_string

print(number_string) # output below
""")

number_string = number.get_string()

print(number_string)

print("\n# We can declare an attribute from the global scope")

print("""
number.is_negative = False

print(number.is_negative) # output below
""")

number.is_negative = False

print(number.is_negative)

print("\n# We can define a function that's outside the class, and initialize it in the class")

print("""
def get_real_number(self):
    return self.real_number

class complex_number():

    def __init__(self, real_number, imaginary_number):
        self.real_number = real_number
        self.imaginary_number = imaginary_number

    def get_string(self):
        return str(self.real_number) + " + " + str(self.imaginary_number) + "i"

    grn = get_real_number # LOOK HERE

number = complex_number(2, 3)

output = number.get_string()

print(output) # output below
""")


def get_real_number(self):
    return self.real_number

class complex_number():

    def __init__(self, real_number, imaginary_number):
        self.real_number = real_number
        self.imaginary_number = imaginary_number

    def get_string(self):
        return str(self.real_number) + " + " + str(self.imaginary_number) + "i"

    grn = get_real_number # LOOK HERE

number = complex_number(2, 3)

output = number.get_string()

print(output) # output below


