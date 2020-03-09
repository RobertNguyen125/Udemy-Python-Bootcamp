import random
player1 = input('Player1! Make your move: ').lower()
rand_num = random.randint(0,2)

if rand_num == 0:
    computer = 'rock'
elif rand_num == 1:
    computer = 'paper'
else:
    computer = 'scissors'
print(f'Computer plays {computer}')

if player1 == computer:
    print('Draw!')
elif player1 =='rock':
    if computer == 'scissors':
        print('Player1 wins')
    else: # because the computer has no other choice, unlike the previous exercise when a human can enter anything
        print('Computer wins')
elif player1 == 'paper':
    if computer == 'rock':
        print('Player1 wins')
    else:
        print('Computer wins')
elif player1 == 'scissors':
    if computer == 'paper':
        print('Player1 wins')
    else:
        print('Computer wins')
else:
    print('Something went wrong')
