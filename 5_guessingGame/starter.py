import random

random_number = random.randint(1,10)  # numbers 1 - 10
input = None

while input != random_number:
    input = input('Please enter your number: ')
    input = int(input)
    if input < random_number:
        print('It is too low')
    elif input > random_number:
        print('It is too high')
    else:
        print('You won')
print(random_number)

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!
