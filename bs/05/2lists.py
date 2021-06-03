list_name = ['Lollipop', 'Bacon', 'Eggs', 'Ice Cream', 'Milk', 'Bread', 'Banana', 'Poop']

print("# We currently have the following list \n")
print(list_name)

print("\n# What if we want to remove a specific item?")
print("# We can use the remove function of list by providing the item we want to remove")

print("""
list_name.remove("Poop") # make sure the item exists or a Value Error will be thrown

print(list_name) # output below
""")

list_name.remove("Poop")

print(list_name)

print("\n# We can remove the last item of the list by using the pop function of list")

print("""
list_name.pop() # no errors will be thrown if list is empty

print(list_name) # output below
""")

list_name.pop()

print(list_name)

print("\n# We can use the very same function to remove an item at a specific index")
print("# Just provide the index of the item you want to remove this time")

print("""
list_name.pop(0)

print(list_name) # output below
""")

list_name.pop(0)

print(list_name)

print("\n# What if we want the index of a particular item?")
print("# Well, use the index function of list and provide the item of interest")
print("# It will return the index of the first item of interest that appears in the list")
print("# If there is no such item you will get a Value Error!")

print("""
index_of_ice_cream = list_name.index("Ice Cream")

print(index_of_ice_cream) # output below
""")

index_of_ice_cream = list_name.index("Ice Cream")

print(index_of_ice_cream)

print("\n# We can use the list copy function on the list we want to copy")
print("# returning a copy of the list, to create a new exact same list")
print("# same thing as using list_name[:]")

print("""
list_copy = list_name.copy()

list_name.pop() # MAKING A POINT HERE

print("list_name", list_name) # output below
print("list_copy", list_copy) # shallow copy
""")
list_name = ['Bacon', 'Eggs', 'Ice Cream', 'Milk', 'Bread']
list_copy = list_name.copy()

list_name.pop()

print("list_name", list_name)
print("list_copy", list_copy)
