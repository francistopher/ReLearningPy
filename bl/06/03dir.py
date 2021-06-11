print("# What if you want to know the 'predefined names'? Call dir without any arguments")
print("# In return you'll get a list of 'predefined names'")

print("""
predefined_names = dir()

print(predefined_names) # output below
""")

predefined_names = dir()

print(predefined_names)

print("\n# Let's say you want to know the names a module defines, you'll import the module")
print("# Then call dir with the module name passed in as an argument, returning an array of names defined")

print("""
import quotes

defined_names = dir(quotes)

print(defined_names) # output below
""")

import quotes, sys

defined_names = dir(quotes)

print(defined_names) # output below

print("# To get the names of built in functions/variables, import builtins and pass it as an argument to dir")

print("""
import builtins

built_in = dir(builtins)

print(built_in) # output below
""")

import builtins

built_in = dir(builtins)

print(built_in)




