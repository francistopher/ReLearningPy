ages = [13, 16, 18, 20, 21]
print('ages = [13, 16, 18, 20, 21]')
print('print(ages)')
print(ages, '\n')

print('print(ages[2])')
print(ages[2])
print('# lists can be indexed, just like strings\n')

print('print(ages[-2:])')
print(ages[-2:])
print('# lists can be sliced, just like strings\n')

print('print(ages[:])')
print(ages[:])
print('# creates a shallow copy of the original list\n')

print('ages2 = ages[:]')
ages2 = ages[:]
print('ages2[0] = 12', '\n# by the way lists are immutable')
ages2[0] = 12
print('print(ages)')
print('print(ages2)')
print(ages)
print(ages2)
print("# see, ages2 is a shallow copy\n")

print('print(ages + ages2)')
print(ages + ages2)
print('# lists support concatenation\n')

