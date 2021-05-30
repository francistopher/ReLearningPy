print("# Looping over just the dictionary, just retrieves the keys")

print("""
dictionary = {"hola1": "nena", "hola2":"baby", "hola3":"mami"}

for key in dictionary:
    print(key) # output below
""")

dictionary = {"hola1": "nena", "hola2":"baby", "hola3":"mami"}

for key in dictionary:
    print(key)

print("\n# Looping over the dictionary.items(), retrieves both the keys and values")

print("""
dictionary = {"hola1": "nena", "hola2":"baby", "hola3":"mami"}

for key, value in dictionary.items():
    print(key, value) # output below
""")

dictionary = {"hola1": "nena", "hola2":"baby", "hola3":"mami"}

for key, value in dictionary.items():
    print(key, value)

print("\n# Looping over the enumeration of the dictionary, retrieves the position indexes and the keys")
print("""
dictionary = {"hola1": "nena", "hola2":"baby", "hola3":"mami"}

for index, key in enumerate(dictionary):
    print(index, key) # output below
""")

dictionary = {"hola1": "nena", "hola2":"baby", "hola3":"mami"}

for index, key in enumerate(dictionary):
    print(index, key) # output below


print("\n# Looping over the enumeration of a list, retrieves the position indexes and the elements")

print("""
listo = ["nena", "baby", "mami"]

for index, element in enumerate(listo):
    print(index, element)
""")

listo = ["nena", "baby", "mami"]

for index, element in enumerate(listo):
    print(index, element)

print("\n# We can nest reversed(), sorted(), set() to get a reversed sorted set (non-repeating) iteration")

print("""
name = ["Christopher", "Joshua", "Francisco", "Francisco"]

for element in reversed(sorted(set(name))):
    print(element) # output below
""")

name = ["Christopher", "Joshua", "Francisco", "Francisco"]

for element in reversed(sorted(set(name))):
    print(element) # output below

print("\n# We can pair the entries from two iterables into one iterable with zip(iterable1, iterable2)")

print("""
name1 = ["Kristopher", "Jericho", "Francisco"]
name2 = ["Maximiliano", "Amadeus", "Francisco"]

for name_1_element, name_2_element in zip(name1, name2):
    print(name_1_element, name_2_element) # output below
""")

name1 = ["Kristopher", "Jericho", "Francisco"]
name2 = ["Maximiliano", "Amadeus", "Francisco"]

for name_1_element, name_2_element in zip(name1, name2):
    print(name_1_element, name_2_element)
