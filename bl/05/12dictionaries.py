print("# Dictionaries don't have values as elements, they have key-value pairs as elements")

print("\nmy_dict = {\"key4\":\"value4\", \"key2\":\"value2\", \"key3\":\"value3\"}\") # the keys must be unique")

my_dict = {"key4":"value4", "key2":"value2", "key3":"value3"}

print("\n# Dictionaries are like lists, except that they're indexed by keys")

print("""
my_value = my_dict["key4"]

print(my_value) # output below
""")

my_value = my_dict["key4"]

print(my_value) # output below

print("\n# Updated a value in a dictionary by assigning a value to an indexed dictionary")

print("""
my_dict["key1"] = "newValue"

print(my_dict) # output below
""")

my_dict["key1"] = "newValue"

print(my_dict)

print("\n# Delete a value from a dictionary using the del statement")

print("""
del my_dict["key3"]

print(my_dict) # output below
""")

del my_dict["key3"]

print(my_dict)

print("\n# Convert the dictionary to a list, but the list won't contain the values")

print("""
the_list = list(my_dict)

print(the_list) # output below
""")

the_list = list(my_dict)

print(the_list)

print("\n# You can convert the dictionary to a list and sort the elements (keys) with just the sorted function")

print("""
the_sorted_list = sorted(my_dict)

print(the_sorted_list) # output below
""")

the_sorted_list = sorted(my_dict)

print(the_sorted_list)

print("\n# See if a key exists or does not exist")

print("""
key3_in_dict = 'key3' in my_dict

key1_not_in_dict = 'key1' not in my_dict

print(key3_in_dict)
print(key1_not_in_dict) # outputs below
""")

key3_in_dict = 'key3' in my_dict

key1_not_in_dict = 'key1' not in my_dict

print(key3_in_dict)
print(key1_not_in_dict) # outputs below


