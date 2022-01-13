# Assingment: Tic Tac Toe Game
# Author: Kaylene Ellinger

def main():
    current_player = player('')
    board = create_board()
    
    while not (winner(board)) or (draw(board)):
        show_board(board)
        turn(board, current_player)
        current_player = player(current_player)
    show_board(board)
    print('\nEnd of Game')

def create_board():
    board = []
    for spot in range(10):
        board.append(spot)
    return board

def show_board(board):   
    print(f'\n{board[1]}|{board[2]}|{board[3]}')
    print('-+-+-')
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print('-+-+-')
    print(f'{board[7]}|{board[8]}|{board[9]}')

    
def player(playing):
    # Since x always starts, if there is no current player playing then we must begin with x
    if playing == '' or playing == 'o':
        return 'x'
    elif playing == 'x':
        return 'o'

def turn(board, current_player):
    spot = int(input(f"\n{current_player}'s turn to choose a sqaure (1-9): "))
    board[spot] = current_player


def winner(board):
    if (board[1] == 'x' and board[2] == 'x' and board[3] == 'x' or 
    board[4] == 'x' and board[5] == 'x' and board[6] =='x' or 
    board[7] == 'x' and board[8] == 'x' and board[9] =='x' or
    board[1] == 'x' and board[5] == 'x' and board[9] == 'x' or
    board[1] == 'x' and board[4] == 'x' and board[7] == 'x' or
    board[2] == 'x' and board[5] == 'x' and board[8] == 'x' or
    board[3] == 'x' and board[6] == 'x' and board[9] == 'x' or
    board[3] == 'x' and board[5] == 'x' and board[7] == 'x'):
        print('\nplayer x is the winner! Thanks for playing!')
    elif (board[1] == 'o' and board[2] == 'o' and board[3] == 'o' or 
    board[4] == 'o' and board[5] == 'o' and board[6] == 'o' or 
    board[7] == 'o' and board[8] == 'o' and board[9] == 'o' or
    board[1] == 'o' and board[5] == 'o' and board[9] == 'o' or
    board[1] == 'o' and board[4] == 'o' and board[7] == 'o' or
    board[2] == 'o' and board[5] == 'o' and board[8] == 'o' or
    board[3] == 'o' and board[6] == 'o' and board[9] == 'o' or
    board[3] == 'o' and board[5] == 'o' and board[7] == 'o'):
        print('\nplayer o is the winner! Thanks for playing!')

def draw(board):
    for spot in range(10):
        if board[spot] != 'x' and board[spot] != 'o':
            return False
    return True


if __name__ == '__main__':
    main()