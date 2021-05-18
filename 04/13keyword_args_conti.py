print("# The values you pass through may be interpreted as members of a tuple, for example ...")

print("""
# look at the *numeros parameter below
# anything after the first argument is considered a member of the tuple "numeros"

def funkier(letra, *numeros):
    print(\"Letra\", letra, \"\\nLos Numeros\")
    for num in numeros:
        print(num, sep=\" \")

funkier("A", 2, 3, 4, 5) # The ouput below
""")

def funkier(letra, *numeros):
    print("Letra", letra, "\nLos Numeros")
    for num in numeros:
        print(num, sep=" ")

funkier("A", 2, 3, 4, 5)

print("\n# You can even pass through values interpreted as members of a dictionary, for example ...")

print("""
# look at the **letras parameter below
# anything passed with an explicit key word for **letras
# is a member of the dictionary "letras"

def funkiest(letra, **letras):
    print(\"Letra\", letra, \"\\nMas Letras\")
    for key in letras:
        print(\"Key:\", key, \"Value:\", letras[key])

funkiest("A", b="B", c="C", d="D", e="E", f="F") # the output below
""")

def funkiest(letra, **letras):
    print("Letra", letra, "\nMas Letras")
    for key in letras:
        print("Key:", key, "Value:", letras[key])

funkiest("A", b="B", c="C", d="D", e="E", f="F")

