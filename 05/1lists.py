print("# Down below we have implemented a list, but it's empty :(")
print("""
list_name = []

print(list_name) # output below
""")

list_name = []

print(list_name)
print("\n# We can add an item to the end of the list one at a time")

print("""
item1 = "Bacon"

list_name.append(item1)
list_name.append("Eggs")

print(list_name) # output below
""")

item1 = "Bacon"

list_name.append(item1)
list_name.append("Eggs")

print(list_name) # output below

print("\n# We can add multiple items from an iterable!")
print("# Firstly, pass a list of items as an argument to the built in iterable function")

print("""
iterable = iter(["Milk", "Bread", "Banana"])
""")

iterable = iter(["Milk", "Bread", "Banana"])

print("# Secondly, slice the list to the part where the items of the iterable will go")
print("# Then assign the iterable to that slice")

print("""
list_name[len(list_name):] = iterable

print(list_name) # output below
""")
list_name[len(list_name):] = iterable

print(list_name)

print("\n# What if you want to add an item to a location other than the end of the list?")
print("# Insert the item by using the insert function of list by providing the index and item")

print("""
item_to_insert = "Lollipop"
insert_at_index = 0

item_to_insert2 = "Ice Cream"
insert_at_index2 = 3

list_name.insert(insert_at_index, item_to_insert)
list_name.insert(insert_at_index2, item_to_insert2)

print(list_name) # Output below
""")

item_to_insert = "Lollipop"
insert_at_index = 0

item_to_insert2 = "Ice Cream"
insert_at_index2 = 3

list_name.insert(insert_at_index, item_to_insert)
list_name.insert(insert_at_index2, item_to_insert2)

print(list_name) # Output below

print("\n# What if the index doesn't exist?")

print("""
list_name.insert(100, "Poop") # goes over? adds it to the end
list_name.insert(-100, "Poop") # goes below? just ignores 

print(list_name) # output below
""")

list_name.insert(100, "Poop")

print(list_name) # output below
