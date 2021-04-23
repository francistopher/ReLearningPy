print(r"print('C:\some\name')")
print("C:\some\name")
print("# But we want to print the entire directory!\n")

print(r"print(r'C:\some\name')")
print(r"C:\some\name")
print("# use the character r at the beginning of the parameter to print the \"raw\" string")
print()

print('print(\"\"\"\\\ni am going\n    to print\nmultiple lines\n\"\"\")')
print("""\
i am going
    to print
multiple lines
""")

print(r"print(3 * 'hello' + 'bob')")
print(3 * 'hello' + 'bob')
print("# prints 'hello' 3 times and with 'bob' appended at the end\n")

print(r"print('py' 'thon')")
print("py" "thon")
print("# two string literals with a blank in between are printed out as one\n")

print("text = ('Hello'\n\t' World')")
print("print(text)")
text = ('Hello'
        ' World')
print(text)
print("# kinda like a single line touple output\n")

print("prefix = 'py'\nprint(py + 'thon')")
prefix = 'py'
print(prefix + "thon")
print("# use the + symbol to concatenate variables")

