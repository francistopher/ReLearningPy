print("# lists and strins are the sequence data types we know so far, there is another one known as the tuple!")
print("# a tuple consists of values seperated by commas")

print("""
first_tuple = 'Christopher', 'Josue', 'Francisco'

print(first_tuple) # output below
""")

first_tuple = 'Christopher', 'Josue', 'Francisco'

print(first_tuple)

print("\n# You can access tuple elements by tuple indexing, just like list indexing")

print("""
first_element = first_tuple[0]

print(first_element) # output below
""")

first_element = first_tuple[0]

print(first_element)

print("\n# Tuples can be nested too! Just like lists")

print("""
nested_tuple = first_tuple, "de la Villa", "Escudero"

print(nested_tuple) # output below
""")

nested_tuple = first_tuple, "de la Villa", "Escudero"

print(nested_tuple)

print("\n# However, tuples are not mutable like lists, they are immutable")

print("""
# The following will cause a type error, uncomment to see for yourself
print(nested_tuple[0] = "Christopher") # This will cause a type error
""")

# print(nested_tuple[0] = "Christopher") # This will cause a type error

print("\n# But they sure can contain mutable objects")

print("""
seeee = ["Christopher Francisco"], ["Is my name!"]

print(seeee) # output below
""")

seeee = ["Christopher Francisco"], ["Is my name!"]

print(seeee)
