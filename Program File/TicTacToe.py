# Tic-Tac-Toe

board = [2, 2, 2,
         2, 2, 2,
         2, 2, 2]
o = 0
x = 1
current_player = int(1)
takenspots = 0
empty = 2
WON = False


# Checks to see if the selected spot is taken
def check_spot(z):
    if board[z] == 1 or 2:
        return True
    else:
        return False


# Checks to see if someone won
def check_won():
    if board[0] and board[1] and board[2] == 0 or 1:
        WON = True
    elif board[0] and board[3] and board[6] == 0 or 1:
        WON = True
    elif board[0] and board[4] and board[8] == 0 or 1:
        WON = True
    elif board[1] and board[4] and board[7] == 0 or 1:
        WON = True
    elif board[2] and board[5] and board[8] == 0 or 1:
        WON = True
    elif board[3] and board[4] and board[5] == 0 or 1:
        WON = True
    elif board[6] and board[7] and board[8] == 0 or 1:
        WON = True
    else:
        WON = False


# Alternates the players back and forth for their moves
def player_check():
    if current_player % 2 == 0:
        move = int(input("Choose your position"))
        make_move(move)
    elif current_player % 2 == 1:
        move = int(input("Choose your position"))
        make_move(move)


# Allows the player to make the move, checks to make sure placing right peice
def make_move(y):
    if check_spot(y) is False:
        print("You can't make that move")
    else:
        if current_player % 2 == 0:
            board[y] = 1
        else:
            board[y] = 0


# Checks available position, if the selected position is available
def available_move():
    for spot in board:
        if board[spot] == 0 or 1:
            takenspots += 1


# Prints the new board
def draw_board():
    print(board)


# Puts all previous functions together to play the game
def play_game():
    print("Beginning a game of TicTacToe")
    if WON is False:
        draw_board()
        player_check()
        check_won()


play_game()
























