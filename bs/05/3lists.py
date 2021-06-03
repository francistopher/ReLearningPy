list_copy =  ['Bacon', 'Eggs', 'Ice Cream', 'Milk', 'Bread']
print("# Get the number of a specific item in a list")
print("# by calling the count function while providing the item of interest")

print("""
list_copy.append("Bread") # APPEND
num_of_items = list_copy.count("Bread")

print(list_copy)
print(num_of_items) # output below
""")

list_copy.append("Bread")
num_of_items = list_copy.count("Bread")

print(list_copy)
print(num_of_items)

print("\n# We can reverse the items in the list by calling the reverse function on the list")

print("""
list_copy.reverse()

print(list_copy) # output below
""")

list_copy.reverse()

print(list_copy)

print("\n# We can sort the list at our liking using the sort function of list")
print("# We can pass no arguments, and it will sort it at will")
print("""
list_copy.sort()

print(list_copy) # output below
""")

list_copy.sort()

print(list_copy)

print("\n# The list can be reversed again using the sort function")
print("# Set the key argument reverse equal to True this time")

print("""
list_copy.sort(reverse=True)

print(list_copy) # output below
""")

list_copy.sort(reverse=True)

print(list_copy)

print("\n# Sort it by length instead! Assign the key argument of key equal to a function name")
print("# This particular function will return the length of each item, the basis of our sorting")
print("# You can also implement your own function")

print("""
def length(item):
    return len(item)

list_copy.sort(reverse=True, key=length) # could've used len instead

print(list_copy) # output below
""")

def length(item):
    return len(item)

list_copy.sort(reverse=True, key=length)

print(list_copy) # output below

print("\n# Now all the items can be removed using the clear function of list")

print("""
list_copy.clear()

print(list_copy, "# Back to where we started on 1list.py") # output below
""")

list_copy.clear()

print(list_copy, "# Back to where we started on 1list.py")
