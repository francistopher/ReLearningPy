print("# Going back to .format")

print("""
message = 'We\'ve previously used the {} to {} our {}'.format(".format", "format", "strings")

print(message) # output below
""")

message = 'We\'ve previously used the {} to {} our {}'.format(".format", "format", "strings")

print(message)

print("\n# We can use { number } to refer to a position of the object passed into .format( ... )")


print("""
message = 'With numbers we are using the {1} to {2} our {0}'.format("strings", ".format", "format")

print(message) # output below
""")

message = 'With numbers we are using the {1} to {2} our {0}'.format("strings", ".format", "format")

print(message)

print("\n# Use keyword arguments with values to defer them to a corresponding {keyword argument}")

print("""
message = 'With keyword arguments we are using the {first} to {second} our {third}'.format(third="strings", first=".format", second="format")

print(message) # output below
""")

message = 'With keyword arguments we are using the {first} to {second} our {third}'.format(third="strings", first=".format", second="format")

print(message) # output below

print("\n# Mix and match indexes and keyword arguments with values to defer them to a corresponding argument")

print("""
message = 'With indexes and keyword arguments we are using the {first} to {second} our {0}'.format("strings", first=".format", second="format")

print(message) # output below
""")

message = 'With indexes keyword arguments we are using the {first} to {second} our {0}'.format("strings", first=".format", second="format")

print(message) # output below

print("\n# A dictionary can be passed in the .format function of string to intropolate the string")
print("# using 0 to access the first argument, [key] to index the values, s to specify the type")
print("""
names = {"first":"Kristofer", "second":"Joshua", "third":"Francisco"}

message = "I wish my name were {0[first]} {0[second]} {0[third]}!".format(names)

print(message) # output below
""")

names = {"first":"Kristofer", "second":"Joshua", "third":"Francisco"}

message = "I wish my name were {0[first]:s} {0[second]:s} {0[third]:s}!".format(names)

print(message)

print("\n# We can use what we've learned to implemented a snippet of the multiplication table")

print("""
for num in range(0, 13):

    twelve = '12 x {0} = {1:}'.format(num, num*12)
    ten = '10 x {0} = {1:}'.format(num, num*10)
    eleven = '11 x {0} = {1:}'.format(num, num*11)

    output = '{0:20} {1:20} {2:20}'.format(ten, eleven, twelve)

    print(output) # outputs below`
""")

for num in range(0, 13):

    twelve = '12 x {0} = {1:}'.format(num, num*12)
    ten = '10 x {0} = {1:}'.format(num, num*10)
    eleven = '11 x {0} = {1:}'.format(num, num*11)

    output = '{0:20} {1:20} {2:20}'.format(ten, eleven, twelve)

    print(output) # outputs below`

print("\n# There's older/manual ways of formatting strings, forget that! We wanna be the kool kid on the block!")
