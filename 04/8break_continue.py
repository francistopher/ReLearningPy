print("# let's say you're iterating through range(0, 10)")
print("# but once you reach the number 3, you want to")
print("# exit out of the for loop")

print("""
for num in range(0, 5):
    if num == 3:
        print("exit out of the for loop")
    print(num)
""")

for num in range(0, 5):
    if num == 3:
        print("exit out of the for loop")
    print(num)

print("\n# well, use the 'break' statement")

print("""
for num in range(0, 5):
    if num == 3:
        break
    print(num)
""")

for num in range(0, 5):
    if num == 3:
        break
    print(num)

print("\n# what if I want to continue straight")
print("# to the next iteration?")

print("""
for num in range(0, 5):
    if num == 3:
        print("continue to the next iteration")
    print(num)
""")

for num in range(0, 5):
    if num == 3:
        print("continue to the next iteration")
    print(num)

print("\n# well, use the 'continue' statement")

print("""
for num in range(0, 5):
    if num == 3:
        continue
    print(num)
""")

for num in range(0, 5):
    if num == 3:
        continue
    print(num)
