print("# We can call methods within methods, also we can make the methods private to the object")
print("# by declaring the method name with __ at the beginning, same goes for attributes/variables")
print("# 2 underscores, to try to call it, uncomment to see for yourelf, i dare you")

print("""
class complex_number:

    def __init__(self, r, i):
        self.__r = r
        self.__i = i

    def __get_r_str(self):
        return str(self.r)

    def __get_i_str(self):
        return str(self.i)

    def get_str(self):
        return self.__get_r_str() + " + " + self.__get_i_str() + "i"

cn = complex_number(2, 3)

output = cn.get_str()

print(output) # output below

# output = cn.__get_i_str() # uncomment to see for yourself
# output = cn.__r
# output = cn.__i
""")

class complex_number:

    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __get_r_str(self):
        return str(self.r)

    def __get_i_str(self):
        return str(self.i)

    def get_str(self):
        return self.__get_r_str() + " + " + self.__get_i_str() + "i"

cn = complex_number(2, 3)

output = cn.get_str()

print(output)

# output = cn.__get_i_str() # uncomment to see for yourself

print("# A class can inherit another 'base' class if it's within its scope")

print("""
class natural_number():
    
    def __init__(self, n):
        self.n = n

    def is_natural(self):
        return self.n >= 1

class whole_number(natural_number):

    def __init__(self, n):
        self.n = n

    def is_whole(self):
        return self.n >= 0

wn = whole_number(0)

print(wn.is_natural()) # output below
""")

class natural_number():
    
    def __init__(self, n):
        self.n = n

    def is_natural(self):
        return self.n >= 1

class whole_number(natural_number):

    def __init__(self, n):
        self.n = n

    def is_whole(self):
        return self.n >= 0

wn = whole_number(0)

print(wn.is_natural()) # output below

print("\n# A class can inherit multiple base classes if they're within its scope!")
print("# Can't inherit both natural and whole because whole already got natural")

print("""
class other():

    def other_method(self):
        return "other_method"

class integer_number(natural_number, other):
    
    def __init__(self, n):
        self.n = n

    def is_integer(self):
        return self.n >= 0 and self.n <= 0

intn = integer_number(-21)

print(intn.is_integer())
print(intn.is_natural())
print(intn.other_method()) # output below
""")

class other():

    def other_method(self):
        return "other_method"

class integer_number(natural_number, other):
    
    def __init__(self, n):
        self.n = n

    def is_integer(self):
        return self.n >= 0 or self.n <= 0

intn = integer_number(-21)

print(intn.is_integer())
print(intn.is_natural())
print(intn.other_method()) # output below
