print("# the following is a basic if and elif statement structure")
print("""
if conditional1:
    statement1
elif conditional2:
    statement2
elif conditional3:
    statement3
""")
print(""" x = -1
if x < 0:
    print("Hello World! 1")
elif x < 1:
    print("Hellow World! 2")
elif x < 2:
    print("Hello World! 3")
""")

x = -1
if x < 0:
    print("Hello World! 1")
elif x < 1:
    print("Hellow World! 2")
elif x < 2:
    print("Hello World! 3")

print("\n# if the if statement's conditional1 isn't true")
print("# the interpreter hops to the next if")
print("# in this case its an elif, stands for else if")
print("# if the conditional of the elif is true, the statement2s are executed")
print("""
x = 0
if x < 0:

    print("Hello World! 1")
elif x < 1:

    print("Hellow World! 2")

elif x < 2:
    print("Hello World! 3")
""")
x = 0
if x < 0:

    print("Hello World! 1")
elif x < 1:

    print("Hellow World! 2")

elif x < 2:
    print("Hello World! 3")

print("\n# if the conditional of the elif is false,")
print("# the interpreter moves to the next elif and so on and so forth")
print("# you can have as many elif statements, but you have to realize")
print("# the chain starts all over again with one if and only the ifs")

print("""
x = 0
if x < 0:
    print("Hello World! 1")
elif x < 1:
    print("Hellow World! 2")
elif x < 2:
    print("Hello World! 3")
if x < 1:
    print("Hello again!")
""")
x = 0
if x < 0:
    print("Hello World! 1")
elif x < 1:
    print("Hellow World! 2")
elif x < 2:
    print("Hello World! 3")
if x < 1:
    print("Hello again!")
