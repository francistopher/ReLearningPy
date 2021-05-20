print("# Lambda expressions are used to create Lambda functions")

print("\n# Lambda functions are syntactically single expression anonymous functions")

print("\nlambda arg1, arg2: arg1 + arg2 # Lambda expression structure")
print("lambda arguments: return # A bit more abstract")

print("\n# Let's create a power function using a lambda expression")
print("power = lambda base, num: base ** num")

print("\nprint(power(2, 3)) # output below")

power = lambda base, num: base ** num
print(power(2, 3))

print("\n# Now here's a documentation string's structure")
print('"""I am a')
print('\nDocumentation String\n"""')

print("\n# Now let's see it in action!")

print("""
def power_func(base, num):
    \"\"\"My implementation 

    of the built inn powow function
    \"\"\"

    return base ** num

print(power_func) # output below
""")
def power_func(base, num):
    """My implementation 

    of the built inn powow function
    """

    return base ** num

print(power_func(2, 3))
