instructor = 'colt'

def hello():
    return f'Hello {instructor}'
print(hello())

def hello2():
    instructor = 'colt'
    return f'Hello {instructor}'
print(hello2())
print(instructor) # this should return an error
