print("# Import all the defined names in the module to access directly (not indirectly)")
print("# by following this pattern, from module_name import *")

print("""
from matho import *

matrix = get_2d_matrix(2, 2) 

print(matrix, "matrix\\n") # output below

transposed_matrix = transpose_2d_matrix(matrix)

print(transposed_matrix, "transposed matrix") # output below
""")

from matho import *

matrix = get_2d_matrix(2, 2) 
print(matrix, "matrix\n") 
transposed_matrix = transpose_2d_matrix(matrix)
print(transposed_matrix, "transposed matrix")

print("\n# In addition of using modules to reuse & declutter your code, you can execute modules as scripts")
print("# Hold your horses, first you have to add the following code to the end of your module")

print("""
if __name__ == "__main__":
    # code to be executed when module is executed
""")

print("# We have the quotes module with the code below")

print("""
if __name__ == "__main__":
    # imported to access arguments
    import sys
    # prints arguments in module execution call
    for index in range(len(sys.argv)):
        print("Argument", index, "=", sys.argv[index])
""")

print("# The code within the if statement above will be executed when you execute quotes.py")
print("# Additionally, you can pass in arguments to alter the output, try it yourself!")

print("""
python quotes.py argument1 argument2 argument3
""")

print("# The code within the if statement will not be run if the module is imported")

print("""
import quotes

print("Que Paso? Nada!") # output below
""")

import quotes

print("Que Paso? Nada!")

print("\n# Seriously, when quotes was imported, the interpreter searched for a built in module with that name")
print("# Nothing found, it then searched for a file named quotes.py in a list of directories")
print("# Which was given by the variable sys.path")

print("\n# If you look at the directory this file is in, you are going to see the directory __pycache__")

print("\n# Where you'll find a compiled version of each module under the name module.version.pyc")






