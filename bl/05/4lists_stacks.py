stack = [2, 7, 3]
reversed_stack = []

def printStack(stack):
    print("|   |")
    reversed_stack = stack.copy()
    reversed_stack.reverse()
    for item in reversed_stack:
        print("|", item, "|")
    else:
        print("|___|")


print("# Lists can be used as stacks, below is a list")

print("""
stack = [2, 7, 3]
""")

print("# Below is a visual representation of this list as a stack")
print("# Where the last element in is the first element out, LIFO! Joseph!\n")

printStack(stack)

print("\n# For the 'last element in', we use the append built in list function")
print("# to add an element to the list, which is the 'last element in'")
print("""
stack.append(0) 

print(stack) # Output below
""")

stack.append(0)

print(stack)

print("""
# Now the list as a stack
""")

printStack(stack)

print("\n# For the 'last element in is the first element out', we use the pop built in") 
print("# list function, pretty self explanatory if you want your stack to remain intact")
print("# if you decide to pull an element from the bottom or right after the last one")
print("# it will tip over or someting, this is what Joseph didn't understand back then")

print("""
stack.pop()

print(stack) # Output below
""")

stack.pop()
print(stack)

print("""
# Now the list as a stack
""")

printStack(stack)

