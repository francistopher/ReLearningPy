print("# A variable can be declared in the except clause to represent an exception instance")
print("# The handled exception instance has arguments accesible through instance.args")
print("# The arguments can be defined upon initialization")

print("""
try:
    raise Exception("Wasabi", "Gigi Hadid")
except Exception as exception_instance:
    instance_type = type(exception_instance)
    instance_arguments = exception_instance.args
    a, b = instance_arguments # unpack values if instance itself can't be converted to string
    print("Instance:", exception_instance)
    print("Instance Type:", instance_type)
    print("Instance Arguments:", instance_arguments)
    print("Argument a:", a)
    print("Argument b:", b) # outputs below
""")

try:
    raise Exception("Wasabi", "Gigi Hadid")
except Exception as exception_instance:
    instance_type = type(exception_instance)
    instance_arguments = exception_instance.args
    a, b = instance_arguments # unpack values if instance itself can't be converted to string
    print("Instance:", exception_instance)
    print("Instance Type:", instance_type)
    print("Instance Arguments:", instance_arguments)
    print("Argument a:", a)
    print("Argument b:", b) # outputs below

print("\n# We've seen exceptions raised right within the try clause, let's raise an exception")
print("# outside the try clause, let's indirectly raise an exception in a function")

print("""
def hot_gal():
    raise Exception("Gigi Hadid")
try:
    hot_gal()
except Exception as wow:
    print(wow.args) # output below
""")

def hot_gal():
    raise Exception("Gigi Hadid")
try:
    hot_gal()
except Exception as wow:
    print(wow.args)

print("\n# Hopefully you've figured out how to raise an exception through brute force")
print("# We can either raise an exception of our own or a built in exception class")

print("""
try:
    # raise Exception("RAISING AN EXCEPTION THROUGH BRUTE FORCE!") # our own
    raise ValueError # built in exception, with no arguments
except Exception as ex:
    print(ex.args) # output below
""")

try:
    # raise Exception("RAISING AN EXCEPTION THROUGH BRUTE FORCE!") # our own
    raise ValueError # built in exception, with no arguments
except Exception as ex:
    print(ex.args)

print("# What if an exception is raised, but you don't have any except clauses handling it")
print("# letting it sneak through. Well you can inject a raise statement in an except clause")

print("""
try:
    raise Exception("Here I am!") # flew right under our noses
except Exception as exp:
    print(exp.args)
""")

try:
    raise Exception("Here I am!")
except Exception as exp:
    print(exp.args)

print("""
try:
    raise Exception("Here I am!") # not so fast
except Exception as exp:
    print(exp.args)
""")

try:
    raise Exception("Here I am!")
except Exception as exp:
    print(exp.args)
    raise
