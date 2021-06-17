print("# Syntax errors are known as parsing errors, where the Python interpreter doesn't understand le syntax")

print("""
print("Python will be able to understand this!") # This will execute

print(Python will be like nah!) # Error will be raised, uncomment to see for yourself
""")

print("Python will be able to understand this!") # This will execute

# print(Python will not understand this!)

print("\n# You uncomment the statement, and execute the script. So what you'll get is")
print("# the file that raised the error, the line of the file that raised the error,")
print("# any subsequent calls that raised the error, and the type of error")

print("""
 File "1errors_exceptions.py", line 11
    print(print(Python will not understand this!))
                       ^
SyntaxError: invalid syntax
""")

print("# Exceptions are errors that are raised during execution with legal syntax, below is a classic error")

print("""
print("Python will execute this 1!") # output below

print("Python will not execute this" + 1 + "!") # Error will be raised, uncomment to see for yourself
""")
print("Python will execute this 1!")

# print("Python will not execute this" + 1 + "!") # Uncomment to see for yourself

print("\n# You uncomment the statement, and execute the script. So what you'll get is")
print("# the file that raised the error, the line that raised the error, and the")
print("# the type of error with a basic explanation of why you fucked up")

print("""
Traceback (most recent call last):
  File "1errors_exceptions.py", line 33, in <module>
    print("Python will not execute this" + 1 + "!") # Uncomment to see for yourself
TypeError: can only concatenate str (not "int") to str
""")

print("\n# How do I handle errors? With a 'try' and 'except' clause. Specify the error type to be handled")
print("# in the except clause. If the code within the 'try' clause raises an error, the code within the except")
print("# clause is executed. If the try clause raises a different type of error, the error isn't handled")

print("""
try:
    x = int("1")
    print("Python will execute this" + x + "!")
except TypeError:
    print("TypeError exception raised!")
""")

try:
    x = int("1")
    print("Python will execute this" + x + "!")
except TypeError:
    print("TypeError exception raised!")

print("\n# You can add as many except clauses to handle as many errors for the given try clause")

print("""
try:
    x = int("one")
    print("Python will execute this" + x + "!")
except TypeError:
    print("TypeError exception raised!")
except ValueError:
    print("ValueError exception raised!")
""")

try:
    x = int("one")
    print("Python will execute this" + x + "!")
except TypeError:
    print("TypeError exception raised!")
except ValueError:
    print("ValueError exception raised!")
