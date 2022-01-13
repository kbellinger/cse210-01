# Assingment: Tic Tac Toe Game
# Author: Kaylene Ellinger

def main():
    board = create_board()
    current_player = player('')

def create_board():
    board = []
    for spot in range(10):
        board.append(spot)

    print(f'{board[1]}|{board[2]}|{board[3]}')
    print('-+-+-')
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print('-+-+-')
    print(f'{board[7]}|{board[8]}|{board[9]}')

def player(playing):
    # Since x always starts, if there is no current player playing then we must begin with x
    if playing == '' or 'o':
        return 'x'
    elif playing == 'x':
        return 'o'



if __name__ == '__main__':
    main()