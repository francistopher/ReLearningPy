print("# Byte mode enables us to read the data written in the form of bytes objects")
print("# Entering multiple key letters/symbols lets us combine modes")

print("""
open('bytes.txt', 'x')

file_object = open('bytes.txt', 'rb+')

file_object.write(b'Christopher Francisco') # notice the b for bytes at the front

fourth_byte = file_object.seek(4)

print("Goes to byte number", fourth_byte + 1, "which is byte", fourth_byte)
""")

open('bytes.txt', 'x')

file_object = open('bytes.txt', 'rb+')

file_object.write(b'Christopher Francisco')

fourth_byte = file_object.seek(4)

print("You start reading from byte number", fourth_byte)

print("\n# Starting from where you seeked, you can read a specific number of bytes by passing the number of bytes")

print("""
character = file_object.read(4)

print(character) # output below
""")

character = file_object.read(4)

print(character) # output below
