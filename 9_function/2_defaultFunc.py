def add(a,b):
    return a+b
def math(a,b, fn=add):
    return fn(a,b)
def subtract (a,b):
    return a-b

print(math(5,2,subtract))

# Define speak below:
def speak(animal='dog'):
    if animal == 'pig':
        return 'oink'
    elif animal == 'duck':
        return 'quack'
    elif animal == 'cat':
        return 'meow'
    elif animal == 'dog':
        return 'woof'
    else:
        return '?'
print(speak('duck'))
