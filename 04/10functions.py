print("# the following is the basic structure of a function")
print("# also i'll introduce docstrings for functions")
print("# along with the syntax to invoke it")
print("""
def func_name(parameters):
    '''This a docstring'''
    more code

func_name(arguments)
""")

print("# let's call a function that prints hello world i'm <name>")
print("""
def hello(name):
    '''prints hello world before my name'''
    print("Hello, World! I'm", name)

hello("Christopher")
""")

def hello(name):  
    '''prints hello wolrd before my name'''
    print("Hello, World! I'm", name)

hello("Christopher")

print("\n# it is also possible to 'assign' the function to a variable")
print("# but you'll still have to pass the same # arguments")

print("""
new_func = hello
new_func("Christopher")
""")

new_func = hello
new_func("Christopher")

print("\n# did you know the hello function returns something?")
print("# it returns 'none' cause it got nothing to return")

print("""
print(new_func('Christopher'))
""")

print(new_func('Christopher'))

print("\n# what if you want to return something?")
print("# the 'return' keyword comes in handy!")

print("""
def name_length(name):
    return len(name)

whats_returned = name_length("Christopher")

print(whats_returned)
""")

def name_length(name):
    return len(name)

whats_returned = name_length("Christopher")

print(whats_returned)
