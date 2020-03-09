# .values(), .keys() and .items() method
me = {'name':'Duc', 'age':28, 'hobby':'gym'}
for k,v in me.items():
    print(k,v)


donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
sum = 0
for v in donations.values():
    sum += v
    print(sum)
