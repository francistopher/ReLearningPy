print("# but the range function can do more")
print("# range(start_inclusive, end_exclusive, step)")
print("# the default 'step' is 1, if the 'step' is changed to 2")
print("# the range sequence increments by 2 instead of 1")
print("""
for num in range(0, 6, 2):
    print(num)
""")

for num in range(0, 6, 2):
    print(num)

print("\n# now iterating through negative numbers")
print("# with a -2 step from 0 to -6")

print("""
for num in range(0, -6, -2):
    print(num)
""")

for num in range(0, -6, -2):
    print(num)

print("\n# iterate over the indices of a sequences with range() and len()")
pets = ['cat', 'panther', 'tiger', 'lion']

print("""
pets = ['cat', 'panther', 'tiger', 'lion', 'cougar', 'cheetah', 'jaguar']
for index in range(0, len(pets), 2):
    print(index, pets[index])
""")

pets = ['cat', 'panther', 'tiger', 'lion', 'cougar', 'cheetah', 'jaguar']
for index in range(0, len(pets), 2):
    print(index, pets[index])
