#from IPython.display import clear_output
import random

def display_board(board):
    #clear_output()
    print(f'   |   |   ')
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print(f'   |   |   ')
    print(f'------------')
    print(f'   |   |   ')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print(f'   |   |   ')
    print(f'------------')
    print(f'   |   |   ')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print(f'   |   |   ')

def player_input():
    while True:
        marker = input("Please pick a marker 'X' or 'O':\n")
        if marker == 'X' or marker == 'O':
            break
        else:
            continue
    return marker

def place_marker(board, marker, position):
    if position <=9 and position >=1:
        board[position] = marker
    else:
        print('Invalid position!')

def win_check(board, mark):
    result = False
    if board[1]==board[2]==board[3]==mark \
        or board[4]==board[5]==board[6]==mark \
        or board[7]==board[8]==board[9]==mark \
        or board[7]==board[4]==board[1]==mark \
        or board[8]==board[5]==board[2]==mark \
        or board[9]==board[6]==board[3]==mark \
        or board[7]==board[5]==board[3]==mark \
        or board[1]==board[5]==board[9]==mark:
            result = True
    return result

def choose_first():
    return random.randint(1,2)

def space_check(board, position):
    while True:
        if position >=1 and position <=9:
            return board[position] == ' '
        else:
            print('Invalid position, continue')
            continue

def full_board_check(board):
    for i in range(9):
        if board[i] == ' ':
            return False
    return True

def player_choice(board):
    next = 0
    while True:
        try:
            next = int(input('Please enter next position:\n'))
        except Exception as e:
            print('Invalid input')
            continue

        if next>=1 and next<=9:
            if space_check(board, next):
                return next
            else:
                print('Position occupied')
                continue
        else:
            print('Invalid position')
            continue

def replay():
    while True:
        play_again = input('Do you want to play again? Y/N:\n')
        if (play_again=='Y'):
            return True
        if (play_again=='N'):
            return False
        else:
            print('Invalid option, again')
            continue

if __name__ == '__main__':
    print('Welcome to Tic Tac Toe!')
    while True:
        print('System randomly select sequence')
        playerNumber = choose_first()
        if playerNumber == 1:
            player1 = player_input()
            if player1 == 'X':
                player2 = 'O'
            else:
                player2 = 'X'
            sequence = {'1':player1,'2':player2}
        else:
            player2 = player_input()
            if player2 == 'X':
                player1 = 'O'
            else:
                player1 = 'X'
            sequence = {'2':player2,'1':player1}
        print(f'{sequence}')

        board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        playerSequence = 0
        while True:
            if full_board_check(board):
                print('Full, no winner')
                break
            #First player:
            if (playerSequence % 2== 0):
                playerFlag = list(sequence.keys())[0]
            else:
                playerFlag = list(sequence.keys())[1]
            playerMark = sequence[playerFlag]
            position = player_choice(board)
            place_marker(board, playerMark, position)
            display_board(board)
            if win_check(board, playerMark):
                print(f'Winner is Player{playerFlag} with mark {playerMark}')
                break
            else:
                playerSequence +=1
                continue

        if not replay():
            break
        else:
            continue
