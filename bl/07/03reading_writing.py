print("# To start reading a file we can simply open a file with the built in open function")
print("# and assign it's return, a file object, to a variable for manipulation")

print("""
file_object = open('open_sesame.txt') # uncomment to see for yourself
""")

# the_file = open('open_sesame.txt')

print("# What do you know! If the file doesn't exist, the statement above will raise an error")
print("# The mode is set to r as in read by default. We can't read a file if it doesn't exist!")
print("# Set the mode to 'x' to create the file, it returns an error if the file exists")

print("""
file_object = open('open_sesame.txt', 'x')
""")

file_object = open('open_sesame.txt', 'x')

print("# Now that the file has been created, let's create a file object to write to the file")
print("# by setting the mode to 'w' for write!")

print("""
file_object = open('open_sesame.txt', 'w')
""")

file_object = open('open_sesame.txt', 'w')

print("# Call the function write on the file object and pass a string as an argument,")
print("# to write the string to the file and return the number of characters written!")

print("""
num_of_char_written = file_object.write("We are writing to the file!\\nYes, really!\\n")

print(f"{num_of_char_written} characters were written to the file.") # output below
""")

num_of_char_written = file_object.write("We are writing to the file!\nYes, really!\n")

print(f"{num_of_char_written} characters were written to the file.")

print("\n# We can write anything to a file as long as it's a string passed to the argument of write")
print("# We can also append anything written to the file by setting the mode to 'a' for append")

print("""
tup = ("You see!", "A tuple was written to the file")

tup_str = str(tup)

file_object.write(tup_str)
""")

tup = ("You see!", "A tuple was written to the file")
tup_str = str(tup)
file_object.write(tup_str)

print("# Now that the file has contents to be read, let's create a file object")
print("# with it's mode set to 'r' for read")

print("""
file_object = open('open_sesame.txt', 'r')
""")

file_object = open('open_sesame.txt', 'r')

print("# Now we can call the read function on the file object to return a string of the file's contents")

print("""
contents = file_object.read()

print(contents) # output below
""")

contents = file_object.read()

print(contents)

print("\n# There is a way to read the file and close the file without calling close")
print("# With with and with as, yes with with and with as, let me show you")

print("""
with open('open_sesame.txt') as file_object:
    contents = file_object.read()
    print(contents) # output below

print("File Closed?", file_object.closed) # output below
""")

with open('open_sesame.txt') as file_object:
    contents = file_object.read()
    print(contents) # output below

print("File Closed?", file_object.closed) # output below


