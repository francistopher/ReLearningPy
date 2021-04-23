print("# so, you want to iterate over a sequence of numbers?")
print("# range() is a built in function that comes in handy")
print("""
for num in range(5):
    print(num)
""")

for num in range(5):
    print(num)

print("\n# range(5) generates 5 values from 0 inclusive to 5 exclusive")
print("# but i want the range to start from another number!")
print("""
for num in range(0, 5):
    print(num)
""")

for num in range(0, 5):
    print(num)

print("\n# but the syntax above displays the same thing!")
print("# look closely at the range function, range (0, 5)")
print("# use the format bellow to start at another number")
print("# range(start_inclusive, end_exclusive)")

print("""
for num in range(5, 10):
    print(num)
""")

for num in range(5, 10):
    print(num)
