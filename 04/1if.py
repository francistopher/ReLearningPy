print("the following is the basic structure of an if-statement")
print("python doesn't require the conditional to be in between ( )")
print("""
if conditional:
    statements
    statements
    statements
# if the conditional is true
# the statements will be executed
# that's basically it
""")

print("# below are 2 if statements")
print("""
x = -1
if x < 0:
    print("Hello, World! :)")
if x < 1:    
    print("Goodbye, World! ;(")
""")
x = -1
if x < 0:
    print("Hello, World! :)")
if x < 1:
    print("Goodbye, World! ;(")
print("\n#if-statements are independent from one another,")
print("#therefore they will both be executed")
print("#even though one comes right after the other")

print("the following is a basic if and elif statement structure")
print("""
if conditional1:
    statement1
    statement1
    statement1
elif conditional2:
    statement2
    statement2
    statement2
elif conditional3:
    statement3
    statement3
    statement3
""")
print(""" 
x = -1
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

print("\n#if the if statement's conditional1 isn't true")
print("#the interpreter hops to the next if")
print("#in this case its an elif, stands for else if")
print("#if the conditional of the elif is true, the statement2s are executed")
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

print("\n#if the conditional of the elif is false,")
print("#the interpreter moves to the next elif and so on and so forth")
print("#you can have as many elif statements, but you have to realize")
print("#the chain starts all over again with one if and only the ifs")

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


print("\n#the following is a basic if, elif, and else statement structure")
print("#there can be no elif or as many elif statements")
print("#there can be an if without an else")
print("#but there can't be an else without an if")
print("""
if conditional1:
    statement1
    statement1
    statement1
elif conditional2:
    statement2
    statement2
    statement2
else:
    statement3
    statement3
    statement3
""")

print("#if not a single of the conditionals of the if or the elifs are true")
print("#the interpreter will go down to the\'chain\' and run whatever")
print("#is in the else's body, its the last resort, no conditional needed for the else")
