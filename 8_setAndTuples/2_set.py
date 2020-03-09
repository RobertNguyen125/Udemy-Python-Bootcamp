# Like a maths sets
# do not have duplicate values
# no order
# cant be accessed by index


a = set({1,2,3,4,5,5,3})
print(a)

# set method
# .add()
a.add(6)
print(a)

# .remove()
a.remove(6)
print(a)

# .discard()
a.discard(7)

maths = {'Duc', 'Tri', 'Linh', 'Vu'}
biology = {'Diep', 'seoton', 'ai do', 'ai vay', 'Duc'}

print(maths | biology)
print(maths & biology)
