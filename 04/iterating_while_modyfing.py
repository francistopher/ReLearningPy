print("# so you want to iterate over a sequence of numbers?")
print("# its suggested to loop over a copy of the collection")
print("# or create a new one")

pets_ages = {'dog':3, 'cat':2, 'raccoon':4}
print(pets_ages)
for pet, age in pets_ages.copy().items():
    if age > 2:
        del pets_ages[pet]

print(pets_ages)

