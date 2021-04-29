print("""# the 'name' to the right of the function name 'name_length' is a parameter 

def name_length(name):
    print(name, ": ", len(name), "letters long.")

# below we are calling the function name_length 
# the name \"Francisco\" to the right of the function name \"name_length\" is an argument

name_length("Francisco")
""")

def name_length(name):
    print(name, ":", len(name), "letters long.")
name_length("Francisco")

print("\n# we can specify a default value for one or more arguments")
print("# by assigning the parameter a value right in the function header")

print("""
def create_house(bed_rooms=1):
    if (bed_rooms > 1):
        print("House created with", bed_rooms, "bedrooms.")
    else:
        print("House created with 1 bedroom.")

create_hourse()
""")

def create_house(bed_rooms=1):
    if (bed_rooms > 1):
        print("House created with", bed_rooms, "bedrooms.")
    else:
        print("House created with 1 bedroom.")
create_house()

print("\n# As you can see above, the number of bed_rooms automagically defaulted to 1")
print("# Now we will set the number of bedrooms ourselves")

print("\ncreate_house(3)\n")
create_house(3)

print("""
# you can assign the default value of bed_rooms outside of the function
i = 20

def create_mansion(bed_rooms=i):
    if (bed_rooms > 1):
        print("Mansion created with", bed_rooms, "bedrooms.")
    else:
        print("Mansion created with 1 bedroom.")

create_mansion()
""")
i = 20
def create_mansion(bed_rooms=i):
    if (bed_rooms > 1):
        print("Mansion created with", bed_rooms, "bedrooms.")
    else:
        print("Mansion created with 1 bedroom.")

create_mansion()

print("""
# the default value is only assigned once,
# if we have a list as the default value and an item was appended to it with every call
# it would never default back to an empty list unless you explicitly empty the list

def print_rooms(room_name, room_names=[]):
    room_names.append(room_name)
    print(room_names)

print_rooms("Red Room")
print_rooms("Green Room")
print_rooms("Blue Room")
""")

def print_rooms(room_name, room_names=[]):
    room_names.append(room_name)
    print(room_names)

print_rooms("Red Room")
print_rooms("Green Room")
print_rooms("Blue Room")
