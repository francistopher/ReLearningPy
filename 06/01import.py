print("# We can declutter and reuse code from other files with, import file_name.py")

import matho

print("\nimport matho # matho.py exists in same directory")

print("\n# Now you can indirectly access anything named in its global scope!")

print("""
matrix = matho.get_2d_matrix(rows=2, columns=3)

print(matrix) # output below
""")

matrix = matho.get_2d_matrix(rows=2, columns=3)

print(matrix)

print("\n# You can access the name function of the module, basic stuff")

print("""
output = matho.__name__

print(output) # output below
""")

output = matho.__name__

print(output) # output below

print("\n# You want to create a bajillion matrices later, assign the function to a local name to use later")

print("""
make_matrix = matho.get_2d_matrix

matrix = make_matrix(rows=2, columns=3)

print(matrix) # output below
""")

make_matrix = matho.get_2d_matrix

matrix = make_matrix(rows=2, columns=3)

print(matrix)

print("\n# What if I want to import a number of items from a module? use from module_name import name")

print("\nfrom matho import get_2d_matrix, transpose_2d_matrix")

from matho import get_2d_matrix, transpose_2d_matrix

print("\n# Remember you would have to manually import __name__ to access it.")

print("""
matrix = get_2d_matrix(rows=2, columns=3)

print(matrix, "# Original Matrix\\n")

transposed_matrix = transpose_2d_matrix(matrix)

print(transposed_matrix, "# Transposed Matrix\\n") # outputs below
""")

matrix = get_2d_matrix(rows=2, columns=3)

print(matrix, "# Original Matrix\n")

transposed_matrix = transpose_2d_matrix(matrix)

print(transposed_matrix, "# Transposed Matrix\n")

print("# We can import a module 'as' a different name")

print("""
import matho as meth # all of meth
from matho as meth import get_2d_matrix # just that

matrix = meth.get_2d_matrix(rows=2, columns=3)

print(matrix) # output below
""")

import matho as meth

matrix = meth.get_2d_matrix(rows=2, columns=3)

print(matrix)

