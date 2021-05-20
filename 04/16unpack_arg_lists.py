print("# Here we have a generator from 1 to 3")

print("\ng = range(1, 4)")

print("\nprint(g) # output below")

g = range(1, 4)

print(g)

print("\n# Pass it as an argument to the list built in function")
print("# A list of the generator g has been created!")

print("\ng_list = list(g)")
print("\nprint(g_list) # output below")

g_list = list(g)

print(g_list)

print("\n# What if we want to unpack the arguments from the list ...")
print("# ... to create a new generator with the values of the list!")
print("\n# Pass the list as an argument to the built in range function")
print("# Not so fast, pass it like this with the * operator, range(*list_name)")

print("\n# This is our sample list with numbers from 1 to 5 this time")
print("\nsample_list = [1, 5]")

sample_list = [1,5]

print("\nnew_g = range(*sample_list)")
print("\nprint(new_g) # output below")

new_g = range(*sample_list)
print(new_g)

print("\n# And we can create a list from this 'new_g' like we did before")

print("\nnew_list = list(new_g)")
print("\nprint(new_list) # output below")

new_list = list(new_g)
print(new_list)

print("\n# Dictionaries can be used to deliver keyword arguments")
print("# Pass the dictionary as an argument using the ** operator")
print("# The dictionary's keys are the argument keywords, and the values are the values")

print("""
d = {"Honda" : "Civic", "Toyota" : "Corolla", "Tesla" : "Model 3"}

def car_sales(Honda, Toyota="Camry", Tesla="Model S"):
    print(Honda, "and", Toyota, "sales are going to get crushed by", Tesla, "sales")

car_sales(**d) # output below
""")

d = {"Honda" : "Civic", "Toyota" : "Corolla", "Tesla" : "Model 3"}

def car_sales(Honda, Toyota="Camry", Tesla="Model S"):
    print(Honda, "and", Toyota, "sales are going to get crushed by", Tesla, "sales")

car_sales(**d)
