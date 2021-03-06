print("# You call a function from the non-local scope to update a non-local variable, it won't update!")

print("""
def christopher():
    
    hunger = "not hungry"
    
    def hungry():
        hunger = "very hungry"

    hungry()
    print("After hungry() call:", hunger)

christopher() # output below
""")

def christopher():
    
    hunger = "not hungry"
    
    def hunger_local():
        hunger = "very hungry"

    hunger_local()
    print("After hungry() call:", hunger)

christopher()

print("\n# You can force a function from the non-local scope to update a non-local variable instead")
print("# With the nonlocal keyword, you can force a non-local variable assigmnet")

print("""
def christopher():
    
    hunger = "not hungry"
    
    def hungry():
        nonlocal hunger # RIGHT HERE!
        hunger = "very hungry"

    hungry()
    print("After hungry() call:", hunger)

christopher() # output below
""")

def christopher():
    
    hunger = "not hungry"
    
    def hungry():
        nonlocal hunger
        hunger = "very hungry"

    hungry()
    print("After hungry() call:", hunger)

christopher()

print("\n# You can add the global keyword instead of the nonlocal to force a global variable")
print("# assignment, meaning that the update will become apparent only in a global call")

print("""
def christopher():
    
    hunger = "not hungry"
    
    def hungry():
        global hunger
        hunger = "very hungry"

    hungry()
    print("After hungry() call:", hunger) # output below

christopher()
print("After christopher() call:", hunger) # output below
""")
def christopher():
    
    hunger = "not hungry"
    
    def hungry():
        global hunger
        hunger = "very hungry"

    hungry()
    print("After hungry() call:", hunger) # output below

christopher()
print("After christopher() call:", hunger) # output below


