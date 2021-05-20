print("# Function Annotations are Optional Metadata Info about the types used by the function")

print("\n# First we must understand how to define the types for the function and it's parameters")
print("The following is the basic structure on how to do this")

print("""
def function_name(arg_1: type, arg_2: type = 'string') -> type:
    return type_object
""")

print("# Now, here is a real implementation!")

print("""
def relearning(physics: str, math: str = "Calculus") -> str:
    studies = "I am currently relearning "
    studies += physics 
    studies += " and "
    studies += math
    studies += " all over again!"
    return studies

print(relearning("Classical Mechanics", "Calculus 2")) # Output below
""")

def relearning(physics: str, math: str = "Calculus") -> str:
    studies = "I am currently relearning "
    studies += physics 
    studies += " and "
    studies += math
    studies += " all over again!"
    return studies

print(relearning("Classical Mechanics", "Calculus 2"))

print("\n# The types are accessible by calling > function_name.__annotations__")

print("""
def relearning2(physics: str, math: str = "Calculus") -> str:
    print("Annotations:", relearning2.__annotations__)
    studies = "I am currently relearning "
    studies += physics 
    studies += " and "
    studies += math
    studies += " all over again!"
    return studies

print(relearning2("Classical Mechanics", "Calculus 2")) # Output below
""")

def relearning2(physics: str, math: str = "Calculus") -> str:
    print("Annotations:", relearning2.__annotations__)
    studies = "I am currently relearning "
    studies += physics 
    studies += " and "
    studies += math
    studies += " all over again!"
    return studies

print(relearning2("Classical Mechanics", "Calculus 2"))

print("\n# Without defining the types, the annotations dictionary will be empty!")

print("""
def relearning3(physics, math = "Calculus"):
    print("Annotations:", relearning3.__annotations__)
    studies = "I am currently relearning "
    studies += physics 
    studies += " and "
    studies += math
    studies += " all over again!"
    return studies

print(relearning3("Classical Mechanics", "Calculus 2")) # Output below
""")

def relearning3(physics, math = "Calculus"):
    print("Annotations:", relearning3.__annotations__)
    studies = "I am currently relearning "
    studies += physics 
    studies += " and "
    studies += math
    studies += " all over again!"
    return studies

print(relearning3("Classical Mechanics", "Calculus 2"))


