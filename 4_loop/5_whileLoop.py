# while loop need to initialise a variable before the loop
# msg = input ('What is the secret password?')
# while msg != 'bananas':
#     print("WRONG!")
#     msg = input('What is the secret password?')
# print('Correct')

x = 1
while x < 11:
    print(x)
    x += 2

from random import randint
number = 0
i = 0
while number!=5:
    i+=1
    number = randint(1,10)
