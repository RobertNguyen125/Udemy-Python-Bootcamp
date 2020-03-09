names = ['Elie', 'Tim', 'Matt']

answer = [name[0] for name in names ]
print(answer)

numbers = range(1,7)
even = [num for num in numbers if num%2==0]
print(even)

l1 =  range(1,5)
l2 = range(3,7)
#create intersection of the 2
intersection = [num for num in l1 if num in l2]
print(intersection)

names = ['Elie', 'Tim', 'Matt']
reverse = [name[::-1].lower() for name in names]
print(reverse)

print([num for num in range(1,101) if num%12==0])

print([[num for num in range(0,3)] for val in range(0,3)])
