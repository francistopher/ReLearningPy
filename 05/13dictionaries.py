print("# This isn't the only way to implement dictionaries, dict = {key : value, ...}")
print("# Dictionaries can be implemented using the built in dict function")

print("""
# Dictionary implemented from sequences of key-value pairs

key_value_sequences = dict([('hey', 'blonde'), ('what up', 'cutiepie'), ('howdy', 'partner')])

print(key_value_sequences) # output below
""")

key_value_sequences = dict([('hey', 'blonde'), ('what up', 'cutiepie'), ('howdy', 'partner')])

print(key_value_sequences) # output below

print("""
# Dictionary implemented from keyword arguments

keyword_arguments = dict(hey='blonde', what_up='cutiepie', howdy='partner')

print(keyword_arguments) # output below
""")

keyword_arguments = dict(hey='blonde', what_up='cutiepie', howdy='partner')

print(keyword_arguments)

print("""
# Dictionary implemented from a dictionary comprehension

dict_comprehension = {x:x * 2 for x in range(1, 6)}

print(dict_comprehension) # output below
""")

dict_comprehension = {x:x * 2 for x in range(1, 6)}

print(dict_comprehension)

