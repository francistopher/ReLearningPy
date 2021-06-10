print("# Byte mode enables us to read the data written in the form of bytes objects")
print("# Entering multiple key letters/symbols lets us combine modes")

print("""
open('bytes.txt', 'x')

file_object = open('bytes.txt', 'rb+')

file_object.write(b'Christopher Francisco') # notice the b for bytes at the front

fourth_byte = file_object.seek(4)

print("You start reading from byte number", fourth_byte, "/ the letter s")
""")

open('bytes.txt', 'x')

file_object = open('bytes.txt', 'rb+')

file_object.write(b'Christopher Francisco')

fourth_byte = file_object.seek(4)

print("You start reading from byte number", fourth_byte, "/ the letter s")

print("\n# Starting where first seeked, you can read a specific number of bytes by passing the number of bytes")

print("""
character = file_object.read(4)

print(character) # output below
""")

character = file_object.read(4)

print(character) # output below

print("\n# You can set where to start seeking a bit more intricately by calling the function seek")
print("# on the file object and pass in arguments offset and whence. Where whence can be 0")
print("(beginning of the file), 1 (current file position), 2 (end of the file). Offsets from whence")

print("""
file_object.seek(-9, 2) # Go to 9th byte from the end

output = file_object.read(7) 

print(output) # output below
""")

file_object.seek(-9, 2) # Go to 9th byte from the end

output = file_object.read(7) 

print(output) # output below

print("\n# With python we can convert between string and JSON, import json first")
print("# Let's convert an object to it's JSON string representation by calling")
print("# the dumps function on json and passing in the object returning a string")

print("""
import json

name = [{'name':{'first':'Christopher', 'middle':'Josue', 'last':'Francisco'}}]

string_representation = json.dumps(name)

print(string_representation) # output below
""")

import json

name = [{'name':{'first':'Christopher', 'middle':'Josue', 'last':'Francisco'}}]

string_representation = json.dumps(name)

print(string_representation) # output below

print("# This json object can be 'dumped' to a file with it's file object as an argument for dump")
print("# Only if the file object is set to writing")

print("""
open('the_json.txt', 'x')

file_obj = open('the_json.txt', 'r+')

json.dump(name, file_obj)
""")

open('the_json.txt', 'x')

file_obj = open('the_json.txt', 'r+')

json.dump(name, file_obj)

print("# We can also read the object from the file and convert it back to a json object by")
print("# calling the load function on json and passing the file object for reading as an argument")

print("""
file_obj = open('the_json.txt')

le_json = json.load(file_obj)

print(le_json) # output below
""")

file_obj = open('the_json.txt')

le_json = json.load(file_obj)

print(le_json) # output below
