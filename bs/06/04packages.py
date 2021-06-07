print("# A parent folder is composed of children folders, a package is composed of modules")
print("# In the current directory, we have the 'meow' package")

print("\n# How does Python know a directory is a package?")
print("# Within the directory there is an __init__.py file")

print("\n# For instance the 'meow' package contains an __init__.py, which contains")

print("""
import roar
import meow
""")

print("# The __init__.py file serves as an import dock where all the ships (modules) are at")
print("# Meaning we can import the package and access all the names from every module")

print("\n# First we have to use relative imports to import each of the files into __init__.py")
print("# Following this pattern, from .file/module import function")

print("""
from .meow import *
from .roar import *
""")

print("# Now that we have the feline package's __init__.py file setup")
print("# We can access all the __init__.py's defined names of the meow and roar modules")
print("# By simply importing the package name, in this case feline")

print("""
from feline import *

meow()
roar()
""")

from feline import *

meow()
roar()

print("\n# What if we want the * to import a particular set of modules?")
print("# In the __init__.py file of the canine package, we have defined list __all__")

print("""
__all__ = ["woof", "bark"]
""")

print("# __all__ contains the name of modules to be imported from package_name import *")
print("# Even though 'meow' is a module in canine, it's not in the list __all__")

print("""
from canine import *

woof.woof()
bark.bark()
# meow.meow() # This will produce an error, uncomment to see for yourself
""")

from canine import *

woof.woof()
bark.bark()
# meow.meow() # This will produce an error, uncomment to see for yourself

print("\n# We can 'go through' a package and access a specific function")

print("""
from canine.meow import meow

meow() # output below
""")

from canine.meow import meow

meow()
