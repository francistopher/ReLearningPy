print("# When we try to print a concatenated string, it can be done like this")

print("""
print("Like", "this", 1, "or", "this", 1)

print("Like this " + str(1) + " or this " + str(1)) # outputs below
""")

print("Like", "this", 1, "or", "this", 1)

print("Like this " + str(1) + " or this " + str(1))

print("\n# However, there is a 'fancier' way of printing a concatenated string")
print("# Using the following structure, print(f\"Content {whatever} content {whatever}")

print("""
uno = 1

print(f"Like this {1} or this {uno}") # output below
""")

uno = 1
print(f"Like this {1} or this {uno}")

print("\n# There is a more complicated way to format your digits across the board")
print("# Where {} are where you want to inject the number with format's arguments being the numbers")
print("# 9 spaces for uno {:-9} and dos rounded by 2 {:2.2}'.format(uno, dos)")

print("""
before_bargain = 12000
after_bargain = 7000

message = 'The original price was {:-9} and after the bargain I bought my car at {:5.2} dollars'.format(before_bargain, after_bargain)

print(message) # output below
""")

before_bargain = 12000
after_bargain = 6999.999

message = 'The original price was {:-9} and after the bargain I bought my car at {:5.2} dollars'.format(before_bargain, after_bargain)

print(message)

print("\n# You're probably wondering { 'why isn't there anything here' :-9}, acceptable reasoning")
print("# Probably because you can have something there, the .format(...) can be ditched entirely")
print("# Leaving you with just the string, but now you must place the variable before the :")

print("""
before_bargain = 12000
after_bargain = 6999.999

message = f'The original price was {before_bargain:-9} and after the bargain I bought my car at {after_bargain:5.2} dollars' # don't forget the f at the front of the string

print(message) # output below
""")

before_bargain = 12000
after_bargain = 6999.999

message = f'The original price was {before_bargain:-9} and after the bargain I bought my car at {after_bargain:5.2} dollars'

print(message)

print("\n# You're probably thinking what the hell is that 7e03?")
print("# Place an f after 5.2 in {:5.2f} to display a float and d after 2 to display an integer")

print("""
before_bargain = 12000
after_bargain = 6999.999

message = f'The original price was {before_bargain:-9f} and after the bargain I bought my car at {after_bargain:5.2f} dollars' # don't forget the f at the front of the string

print(message) # output below
""")

before_bargain = 12000
after_bargain = 6999.999

message = f'The original price was {before_bargain:-9f} and after the bargain I bought my car at {after_bargain:5.2f} dollars' # don't forget the f at the front of the string

print(message) # output below



