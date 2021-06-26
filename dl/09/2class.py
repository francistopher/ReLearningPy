print("# Before you have an object, you must have a class. Here's a basic structure of a class.")

print("""
class class_name:

    class_attribute = 420

    def class_function():
        return 'class_function return'
""")
class class_name:
    """ class docstrings """
    class_attribute = 420

    def class_function():
        return 'class_function return'

print("# The attribute refences can be assigned to")

print("""
class_name.class_attribute = 421
    
print(class_name.class.attribute) # output below
""")

class_name.class_attribute = 421
    
print(class_name.class_attribute) # output below

print("\n# We can also access these attribute references and functions from the global scope")

print("""
output = str(class_name.class_attribute)
output += "\\n" + class_name.class_function()
output += "\\n" + class_name.__doc__

print(output) # output below
""")

output = str(class_name.class_attribute)
output += "\n" + class_name.class_function()
output += "\n" + class_name.__doc__

print(output) # output below

print("\n# With a class, you can build an object! An object is a class that has come to life")
print("# with it's own unique attributes (states) and functions (behaviors), through instantiation")

print("""
class_one = class_name() # Instantiation to the left of =
class_two = class_name()

class_one.class_attribute = 421

print("Class one attribute", class_one.class_attribute)
print("Class two attribute", class_two.class_attribute) # outputs below
""")

class_one = class_name() # Instantiation to the left of =
class_two = class_name()

class_one.class_attribute = 421

print("Class one attribute", class_one.class_attribute)
print("Class two attribute", class_two.class_attribute)

print("\n# Wait what?, they don't seem unique! Yes that's because we're supposed to declare")
print("# the class with an init function to create an 'empty' object, with the 'self' (own object)")
print("# being a parameter in the init function, where you declare it's own attributes")

print("""
class class_name():

    def __init__(self): # UPDATED
            self.class_attribute = 420

    def class_function():
        return 'class_function return'
""")

class class_name():

    def __init__(self): # UPDATED
            self.class_attribute = 420

    def class_function(self):
        return 'class_function return'

print("# Now the objects should be unique, don't forget to add the self parameter for functions")
print("# to make them unique to the instantiation of classes too!")


print("""
class_one = class_name() # Instantiation to the left of =
class_two = class_name()

class_one.class_attribute = 421

print("Class one attribute", class_one.class_attribute)
print("Class two attribute", class_two.class_attribute) # outputs below
""")

class_one = class_name() # Instantiation to the left of =
class_two = class_name()

class_one.class_attribute = 421

print("Class one attribute", class_one.class_attribute)
print("Class two attribute", class_two.class_attribute)
