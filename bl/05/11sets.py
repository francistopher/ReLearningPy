print("There is a data type for sets known as set, an unordered collection with no duplicate elements")

print("""
first_set = {'maybe', 'maybe not', 'maybe', 'maybe not'}

print(first_set) # output below with no duplicates
""")

first_set = {'maybe', 'maybe not', 'maybe', 'maybe not'}

print(first_set)

print("\n# We can create a set from letters in words, set(word_with_letters)")

print("""
a = set("california")
b = set("florida")

print(a)
print(b) # output below
""")

a = set("california")
b = set("florida")

print(a)
print(b)

print("\n# Letters in a but not in b")

print("""
a_minus_b = a - b

print(a_minus_b) # output below
""")

a_minus_b = a - b

print(a_minus_b) # output below

print("\n# Letters in a or b or both")

print("""
a_or_b_or_both = a | b

print(a_or_b_or_both) # output below
""")

a_or_b_or_both = a | b

print(a_or_b_or_both)

print("\n# Letters in both a & b")

print("""
a_and_b = a & b

print(a_and_b) # output below
""")

a_and_b = a & b

print(a_and_b)

print("\n# Letters in a or b but not both")

print("""
a_or_b_not_both = a ^ b

print(a_or_b_not_both) # output below
""")

a_or_b_not_both = a ^ b

print(a_or_b_not_both)

print("\n# You've heard about list comprehensions before, what about set comprehensions?")

print("""
people = {x for x in 'california' if x is in 'florida'} # same thing as a & b

print(people) # output below
""")

people = {x for x in 'california' if x in 'florida'}

print(people) # output below
