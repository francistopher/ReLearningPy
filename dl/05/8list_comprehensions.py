print("# Here is one way to generate a list of squares from 1 to 5")

print("""
squares = []

for x in range(1, 6):
    squares.append(x**2)

print(squares) # output below
""")

squares = []

for x in range(1, 6):
    squares.append(x**2)

print(squares) # output below

print("\n# Here is a fancier way to generate a list of squares from 1 to 5, [operation for element in iterator]")
print("# In the body you manipulate the element, which then is appended to the list")

print("""
squares = []

squares = [x**2 for x in range(1, 6)]

print(squares)
""")

squares = []

squares = [x**2 for x in range(1, 6)]

print(squares)

print("\n# Can a list comprehension replace a nested list? You betcha! Below it's done plainly.")

print("""
multiply_unequal_digits = []

for x in [1, 2, 3]:
    for y in [1, 2, 3]:
        if x == y:
            multiply_unequal_digits.append(x*y)

print(multiply_unequal_digits)
""")

multiply_unequal_digits = []

for x in [1, 2, 3]:
    for y in [1, 2, 3]:
        if x == y:
            multiply_unequal_digits.append(x*y)

print(multiply_unequal_digits)

print("""
# To accomplish the same thing but using a fancier method, follow the format below
# [operation for element1 in iterator1 for element2 in iterator2 conditional1]

multiply_unequal_digits = []

multiply_unequal_digits = [x * y for x in [1, 2, 3] for y in [1, 2, 3] if x == y]

print(multiply_unequal_digits)
""")

multiply_unequal_digits = []

multiply_unequal_digits = [x * y for x in [1, 2, 3] for y in [1, 2, 3] if x == y]

print(multiply_unequal_digits)

print("\n# If the final operation is going to be in a tuple, make sure it's parenthesized!")

print("""
# powers_of_2_from_1_to_5 = [x, x**2 for x in range(1, 6)] will error out

powers_of_2_from_1_to_5 = [(x, x**2) for x in range(1, 6)]

print(powers_of_2_from_1_to_5)
""")

powers_of_2_from_1_to_5 = [(x, x**2) for x in range(1, 6)]

print(powers_of_2_from_1_to_5)
