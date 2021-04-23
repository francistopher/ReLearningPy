print('name = "Christopher"')
name = "Christopher"
print("print(name[0])")
print(name[0])
print("print(name[5])")
print(name[5])
print("# Accessing specific characters from a string based on their index\n")

print('print(name[-1])')
print(name[-1])
print('print(name[-2])')
print(name[-2])
print("# Access specific characters starting from the back\n")

print('print(name[0:5])')
print(name[0:5])
print("# [from the start : character before it]")
print("# [inclusive : to exclusive]\n")

print('print(name[:5])')
print(name[:5])
print('# [from the start : character before it]\n')

print('print(name[5:])')
print(name[5:])
print('# [from the start : to the end]\n')

print('print(name[:5], name[5:], sep="")') 
print(name[:5], name[5:], sep="")
print("# That's my name!\n")

print('print(name[-2:])')
print(name[-2:])
print('# name[circle to the back : ]\n')

print('print(name[20])')
print('# that ^ will throw an error, uncomment and check for yourself\n')
#print(name[20])

print('print(name[4:20])')
print('# that ^ will NOT throw an error, you see')
print(name[4:20])

print('\nname[0] = "J"')
print('# that ^ will throw an error, uncomment and check for yourself')
print("# can't assign an indexed string to a new value\n")
#name[0] = 'j'

print('print("K" + name[2:])')
print("K" + name[2:])
print('# need a new string? create one!\n')

print('p = "python"')
p = "python"
print('print(len(p))')
print(len(p))
print('# my python is about that size, hahahaha')
