print("# Arguments can be passed to a function by position or keyword, for example")

print("""
def meal(food, drink, sauce):
    print("I have", sauce, "on my", food, "while drinking a sip of", drink)

meal("Burger", "Soda", sauce="Ketchup") # Output below
""")

def meal(food, drink, sauce):
    print("I have", sauce, "on my", food, "while drinking a sip of", drink)

meal("Burger", "Soda", sauce="Ketchup")

print("\n# A function's parameter may be a '/' and/or an '*' instead of a word")

print("\n# When a '/' is present, all the arguments before the '/' must be positional only")

print("""
def meal2(food, drink, sauce, /):
    print("I eat", food, "with", sauce, "while drinking", drink)

meal2("tacos", "lemonade", "wasabi") # output below
""")

def meal2(food, drink, sauce, /):
    print("I eat", food, "with", sauce, "while drinking", drink)

meal2("tacos", "lemonade", "wasabi")

print("\nWhich means, the following won't work")

print("""
meal2("tacos", "lemonade", sauce="wasabi") # uncomment to see for yourself
""")

#meal2("tacos", "lemonade", sauce="wasabi")

print("# When an '*' is present, all the arguments after the '*' must be keyword-only")

print("""
def meal3(*, food, drink, sauce):
    print("I have", sauce, "on my", food, "while drinking a sip of", drink)

meal3(sauce="Mustard", food="Hot Dog", drink="Cola") # Output below
""")

def meal3(*, food, drink, sauce):
    print("I have", sauce, "on my", food, "while drinking a sip of", drink)

meal3(sauce="Mustard", food="Hot Dog", drink="Cola")

print("\n# Which means, the following won't work")

print("""
meal3("Mustard", "Hot Dog", "Cola") # uncomment to see for yourself
""")

#meal3("Mustard", food="Hot Dog", drink="Cola")

print("# Now, a combination of '/' and '*'")

print("""
def meal4(food, /, drink, *, sauce):
    print("I'm eating a", food, "with some", sauce, "while drinking", drink)

# anything in between '/' and '*' can be either positional or keyword

meal4("Sandwich", "Juice", sauce="Mayonnaise") # output below
""")

def meal4(food, /, drink, *, sauce):
    print("I'm eating a", food, "with some", sauce, "while drinking", drink)

meal4("Sandwich", "Juice", sauce="Mayonnaise")

print("What about the '*' coming before the '/'?")

print("""
# The following produces an error because
# doesn't know if the 2nd argument is either positional or keyword only

def meal5(food, *, drink, /, sauce):
    print("I'm eating a", food, "with some", sauce, "while drinking", drink)
""")
