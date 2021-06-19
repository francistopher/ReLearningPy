print("# Whether or not an exception is raised in the try clause, we can define clean-up actions")
print("# within the finally clause, even if you don't mess up you'll have an excuse for messing up")

print("""
try:
    print("Mentally setting yourself up for failure")
    # raise Exception("Mentally setting yourself up for failure") # uncomment to see for yourself
finally:
    print("It was my wifi's fault!")
""")

try:
    print("Mentally setting yourself up for failure")
finally:
    print("It was my wifi's fault!")

print("\n# If from the try clause we want to 'jump' to another line, a glance will be taken at the")
print("# finally clause and if we can 'jump' to another line, we'll jump from there, keep in mind")
print("# the finally clause is always executed after the except or the else clause is executed")

print("""
def van_halen_jump():
    try:
        return False
    finally:
        return True

output = van_halen_jump()
print(output) # output below
""")


def van_halen_jump():
    try:
        return False
    finally:
        return True

output = van_halen_jump()

print(output)

print("# The with statement, as we've seen before, allows object to be used with a guarantee to be cleaned up")

print("""
with open('text.txt') as f:
    for line in f:
        print(line, end="")

print("\\nIs closed?", f.closed) # output below
""")

with open('text.txt') as f:
    for line in f:
        print(line, end="")

print("\nIs closed?", f.closed)
