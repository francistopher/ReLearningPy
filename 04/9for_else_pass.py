print("# after the for statement iterates through all the numbers,")
print("# i want it to execute a statement afterwards")
print("""
for num in range(5):
    if num == 5:
        break
    print(num)
print("execute statement")
""")

for num in range(5):
    if num == 5:
        break
    print(num)
print("execute statement")

print("\n# oh, that's a cheap way of handling it")
print("# python offers a more syntactically pleasing way to do it")
print("# so any time the for finished the run")
print("# it falls through the else afterwards")

print("""
for num in range(5):
    if num == 5:
        break
    print(num)
else:
    print("execute statement")
""")

for num in range(5):
    if num == 5:
        break
    print(num)
else:
    print("execute statement")

print("\n# what does the 'pass' statement do? well it doesn't do anything")
print("# it's just a placeholder to remind you where you should add code")

print("""
if 1 == 1:
    pass
    print('one')
""")

if 1 == 1:
    pass
    print('one')
