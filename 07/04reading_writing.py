print("We can write and read the file with a single file object by setting the file object's mode to 'r+'")

print("""
open('abba.txt', 'x')

file_object = open('abba.txt', 'r+')

file_object.write('The Winner Takes It All!\\n')

contents = file_object.read()
print(contents) # output below
""")

open('abba.txt', 'x')

file_object = open('abba.txt', 'r+')

file_object.write('The Winner Takes It All!\n')

contents = file_object.read()
print(contents) # output below

print("# Read the file one line at a time by calling the function readline on the file object")
print("# Before we do so we have to add more text to the file because we already read the file")

print("""
file_object.write('Dancing Queen\\nTake A Chance On Me\\nSuper Trouper\\n')

for i in range(3):
    contents = file_object.readline()
    print(i, contents) # output below
""")

file_object.write('Dancing Queen\nTake A Chance On Me\nSuper Trouper\n')

for i in range(3):
    contents = file_object.readline()
    print(i, contents) # output below

print("\n# I lied, the file has already been read entirely, we have to close it to reread it again")

print("""
file_object.close()
print("Is file_object closed?", file_object.closed)

file_object = open('abba.txt', 'r+')

for i in range(3):
    contents = file_object.readline()
    print(i, contents) # output below

object_file.close()
""")

file_object.close()
print("Is file_object closed?", file_object.closed)

file_object = open('abba.txt', 'r+')

for i in range(3):
    contents = file_object.readline()
    print(i, contents) # output below

file_object.close()
