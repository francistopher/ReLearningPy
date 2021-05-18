print("We have a function with multiple parameters")

print("""
def funk(uno, dos="dos", tres="tres"):
    print(uno)
    print(dos)
    print(tres)""")

def funk(uno, dos="dos", tres="tres"):
    print(uno)
    print(dos)
    print(tres, "\n")

print("\nAll of these will work")

print("""
funk(1)
funk(dos=2, uno=1)
funk(1, tres=3, dos=2)""")

print("\n# Output of funk(1)")
funk(1)

print("# Output of funk(dos=2, uno=1)")
print("# In this case you have to type all the keyword arguments explictly")
funk(dos=2, uno=1)

print("# Output of funk(1, tres=3, dos=2)")
print("# The last explicitly typed keyword arguments can be unordered")
funk(1, tres=3, dos=2)


# Uncomment to check for yourself`

print("All of these will NOT work, uncomment to check for yourself")

#funk()
#funk(uno=1, 2)
#funk(1, uno=1)
#funk(quattro=4)

print("""
funk() # can't be empty
funk(uno=1, 2) # explicitly typed keyword argument can't come before an implicitly typed keyword argument
funk(1, uno=1) # no duplicates
funk(quattro=4) # wtf is this, there's no quattro""")
