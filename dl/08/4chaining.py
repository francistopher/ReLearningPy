print("# None or an exception handled can be used to raise another exception.")
print("# Like passing the baton, your teamate drops it, and you're both blamed for it")

print("""
def funky():
    raise ValueError

try:
    funky() # passed the baton
except ValueError as ve:
    raise RuntimeError("It's the calculator's fault!") from ve # gets blamed""")

print("""
Traceback (most recent call last):
  File "4chaining.py", line 8, in <module>
    funky() # passed the baton
  File "4chaining.py", line 5, in funky
    raise ValueError
ValueError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "4chaining.py", line 10, in <module>
    raise RuntimeError("It's the calculator's fault!") from ve # drops the baton
RuntimeError: It's the calculator's fault!
""")

print("# When you're raising an exception from None, you ain't got someone to blame")

print("""
try:
    open('akuna matata') # passes batton
except OSError:
    raise RuntimeError from None # takes the blame""")

print("""
Traceback (most recent call last):
  File "4chaining.py", line 41, in <module>
    raise RuntimeError from None # takes the blame
RuntimeError
""")

print("# Python comes with built in errors such as ValueError, you can create your own custom Errors")

print("""
class DaddyError(Exception):
    \"\"\"Base Class Exceptions\"\"\"
    pass

class SoyBoyError(DaddyError):
    \"\"\"Exception raised for being a Soy Boy

    Attributes:
        expression - input expression in which the error occurred
        message - explanation for the error
    \"\"\"

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
""")
