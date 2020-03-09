# Tuple:
# - an ordered collection for grouping of items
# - faster than list
# - safer than list because it cant be changed
# - valid to be keys for dictionary

numbers = (1,2,3,4) # -> immutable: cant be updated or changed
print(numbers[1])

# looping
names =('Duc', 'Tri', 'Linh', 'Vu')
for name in names:
    print(name)

names =('Duc', 'Tri', 'Linh', 'Vu')
i = len(names)-1
while i >= 0:
    print(names[i])
    i -= 1

# method:
#.count(): how many times an item appear in a tuple
#.index():
# slciing is similar to list
