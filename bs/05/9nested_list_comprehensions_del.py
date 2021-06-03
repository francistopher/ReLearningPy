print("# We've used list comprehensions to generate a list, now let's generate a nested list")

print("""# We are going to start off simple, a 2 by 3 matrix or 2 rows 3 columns

matrix = []

for x in range(1, 3):
    inner_row = []
    for y in range(1, 4):
        inner_row.append(x * y)
    matrix.append(inner_row)

print(matrix) # output below
""")

matrix = []

for x in range(1, 3):
    inner_row = []
    for y in range(1, 4):
        inner_row.append(x * y)
    matrix.append(inner_row)

print(matrix)

print("\n# Here is the list comprehension implementation, really abstract [ [inner_for_loop] outer_for_loop]")
print("# Less abstract [ [operations_on_elements for element2 in iterator2] for element1 in iterator1]")

print("""
matrix = []

matrix = [[x*y for y in range(1, 4)] for x in range(1, 3)]

print(matrix) # output below
""")

matrix = []

matrix = [[x*y for y in range(1, 4)] for x in range(1, 3)]

print(matrix)

print("\n# Don't understand? We can break the outer list comprehension into a for loop")
print("# and still maintain the inner list comprehension")

print("""
matrix = []

for x in range(1, 3):
    matrix.append([x*y for y in range(1, 4)])

print(matrix) # output below
""")

matrix = []

for x in range(1, 3):
    matrix.append([x*y for y in range(1, 4)])

print(matrix) # output below

print("\n# If we break the inner list comprehension into a for loop")
print("# We get back to the original nested for loops, back to square 1")

print("\n# Remember when we used pop() to return and remove the last value in a list")
print("# Remember when we used remove(index) to remove the value at that index in a list")
print("# There's another way, using the del statement, del list_name[slice]")

print("""
del matrix[0][2] # from the first list in the matrix, delete the 3rd element

print(matrix) # output below
""")

del matrix[0][2]
print(matrix)

print("\n# Not only can we remove elements one at a time, we can slice them out of the list!")

print("""
del matrix[1][1:3] # from the second list in the matrix delete the last 2 elements

print(matrix) # output below
""")

del matrix[1][1:3]
print(matrix)
