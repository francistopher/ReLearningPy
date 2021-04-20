ages = [13, 16, 18, 20, 21]
print('ages = [13, 16, 18, 20, 21]')
print('print(ages)')
print(ages, '\n')

print('print(ages[2])')
print(ages[2])
print('lists can be indexed, just like strings\n')

print('print(ages[-2:])')
print(ages[-2:])
print('lists can be sliced, just like strings\n')

print('print(ages[:])')
print(ages[:])
print('creates a shallow copy of the original list\n')

print('ages2 = ages[:]')
ages2 = ages[:]
print('ages2[0] = 12', '# by the way lists are immutable')
ages2[0] = 12
print('print(ages)')
print('print(ages2)')
print(ages)
print(ages2)
print("see, ages2 is a shallow copy\n")

print('print(ages + ages2)')
print(ages + ages2)
print('lists support concatenation\n')

print('print(ages2[0])')
print(ages2[0])
print('ages2[0] = 13')
print(ages2[0])
print('so like before, lists are immutable\n')

def agesAppend():
    print('print(ages)\n', ages, sep='')
agesAppend()
print('ages.append(23)')
ages.append(23)
agesAppend()
print('use append function to add values to list\n')

print('print(ages)')
print(ages)
print("ages[0:2] = ['k']")
ages[0:2] = ['k']
print("print(ages)")
print(ages)
print('slices of lists can be assigned to\n')

print('print(len(ages))')
print(len(ages))
print('the length of the list ages is', len(ages), '\n')

print('ages[0:1] = [[17.5, 17.75]]')
ages[0:1] = [[17.5, 17.75]]
print('print(ages)')
print(ages)
print('nested lists are possible\n')

print('this is just an intro to lists')
