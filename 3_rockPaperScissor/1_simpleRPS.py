player1 = input('Player 1:')
print('**No Cheating** \n \n' * 20)
player2 = input('Player 2:')

if player1 == player2:
    print("Draw")
elif player1 != player2:
    if player1 == 'rock':
        if player2 == 'scissor':
            print('Player 1 wins')
        else:
            print("Player 2 wins")
    if player1 == 'scissor':
        if player2 == 'paper':
            print('Player 1 wins')
        else:
            print('Player 2 wins')
    if player1 == 'paper':
        if player2 == 'rock':
            print('Player 1 wins')
        else:
            print('Player 2 wins')
else:
    print('Something Wrong')
