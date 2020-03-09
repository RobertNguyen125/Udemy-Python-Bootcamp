# {___:___ for ___ in ____}
#1
numbers = dict(first=1, second=2, third=3)
squared_nums = {k:v**2 for k,v in numbers.items()}
print(squared_nums)

#2
num = {num: num**2 for num in range(1,6)}
print(num)
#3
str1 ='ABC'
str2 ='123'
combo = {str1[i]:str2[i] for i in range(0,len(str1))}
print(combo)

# conditional logic
me = {'name':'Duc', 'age':28, 'hobby':'gym'}
yelling_me = {(k.upper() if k is 'name' else k):(v.upper() if type(v) is str else v) for k,v in me.items()} # error message that 28 is int, no upper() method
print(yelling_me)

even_odd = {num:('even' if num%2==0 else 'odd') for num in range(100)}
print(even_odd)
