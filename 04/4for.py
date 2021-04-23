print("# the following is the basic structure of a for statement / for loop")
print("""
for item in sequence_of_items:
    statements
""")

print("# for statements in Python iterate through the items of any sequence")
print("# in the order they appear")
print("""
pets = ['cat', 'dog', 'raccoon']
for pet in pets:
    print(pet, len(pet))
""")

pets = ['cat', 'dog', 'raccoon']
for pet in pets:
    print(pet, len(pet))

print("\n# if you need to iterate over a sequence of numbers")
print("# the range() build in function comes in handy")
print("""
for num in range(5):
    print(num)
""")

for num in range(5):
    print(num)
