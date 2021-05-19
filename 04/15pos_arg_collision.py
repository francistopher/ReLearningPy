print("# You'll have an error if you have a positional argument 'name'")
print("# and a **variable with 'name' as a key, the multiple 'name' is confusing")

print("""
def get_name(name, **full_name): # get_name(name, key1_as_var, key2_as_var, ...)
   return 'name' in full_name

print(get_name("Chris", **{"name":"Chris"})) # uncomment to see for youself
""")

def get_name(name, **full_name): # get_name(name, key1_as_var, key2_as_var, ...)
   return 'name' in full_name

# print(get_name("Chris", **{"name":"Chris"}))

print("# To solve this you can change the key to not be 'name'")
print("# Or you can insert a '/' in between the parameters")
print("# Makes the first paramater as THE ONLY positional argument!")

print("""
def get_nombre(name, /, **full_name): # get_nombre(name, /, key1, key2, ...)
    return 'name' in full_name

print(get_nombre("Chris", **{"name":"Chris"})) # output below
""")

def get_nombre(name, /, **full_name): # get_nombre(name, /, key1, key2, ...)
    return 'name' in full_name

print(get_nombre("Chris", **{"name":"Chris"}))




