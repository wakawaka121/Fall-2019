###
### Author: Derek Tominaga
### Description: This is 1D chess game
### prints the 1x9 board and draws it with graphics
### using list, and updateing after input is validated.
### The list changes as the pieces move "indexs" in the list
###

from graphics import graphics

W_KNIGHT = 'WKn'
W_KING   = 'WKi'
B_KNIGHT = 'BKn'
B_KING   = 'BKi'
EMPTY    = '   '
WHITE    = 'White'
BLACK    = 'Black'
LEFT     = 'l'
RIGHT    = 'r'

def is_valid_move(board, position, player):
    '''
    This function takes 3 parameters and determines if
    the move is allowed
    board = list of the 1x9 board (0-8 index)
    position = index piece to be validated (is it that players piece)
    player = the players whos turn it is
    '''
    if player == WHITE:
        if (position) not in range(len(board)):
            return False
        elif board[position] == W_KNIGHT:
            return True
        elif board[position] == W_KING:
            return True
        else:
            return False
    elif player == BLACK:
        if (position) not in range(len(board)):
            return False
        elif board[position] == B_KNIGHT:
            return True
        elif board[position] == B_KING:
            return True
        else:
            return False
def move_knight(board, position, direction):
    '''
    This function takes 3 arguments to determines knight movement
    board = list of the 1x9 board (0-8 index)
    position = the index of the knight being moved
    direction = the direction the knight if moved
    '''
    knight = board[position]
    if direction == LEFT:
        position -= 2
        if position in range(len(board)):
            board[position + 2] = EMPTY
            board[position] = knight
    if direction == RIGHT:
        position += 2
        if position in range(len(board)):
            board[position - 2] = EMPTY
            board[position] = knight
def move_king(board, position, direction):
    '''
    This function takes 3 parameters to determine how a king will move
    board = list of the 1x9 board (0-8 index)
    position = the validated index refrencing the piece
    direction = indicates if valid direction piece moves
    '''
    king = board[position]
    if direction == LEFT:
        if (position - 1) in range(0, len(board)):
            condition = True
            board[position] = EMPTY
            position -= 1
            while condition == True:
                if board[position] != EMPTY:
                    board[position] = king
                    condition = False
                elif board[position] == EMPTY and (position - 1) >= 0:
                    position -= 1
                else:
                    board[position] = king
    elif direction == RIGHT:
        if (position + 1) in range(0, len(board)):
            condition = True
            board[position] = EMPTY
            position += 1
            while condition == True:
                if board[position] != EMPTY:
                    board[position] = king
                    condition =  False
                elif board[position] == EMPTY and (position + 1) <= 8:
                    position += 1
                else:
                    board[position] = king
def print_board(board):
    '''
    This function takes one parameter and prints
    the chess board in the command line
    board = list of the 1x9 board (0-8 index)
    '''
    print ("+" + "-" * 53 + "+")
    piece_layout = "| "
    for i in range (len(board)):
        piece_layout += board[i] + " | "
    print (piece_layout)
    print ("+" + "-" * 53 + "+")
def draw_board(board, gui):
    '''
    This function takes two parameters inorder to display
    graphics of the game and updates as the game progresses
    board = list of the 1x9 board (0-8 index)
    gui = a graphics object used to draw
    '''
    space_seperator = 26
    gui.rectangle (25, 100, 650, 60, "firebrick3")
    gui.text(225, 25, "1 Dimensional Chess", "green4", 25)
    while space_seperator < 675:
        gui.line(space_seperator, 100, space_seperator, 160, "black", 2)
        space_seperator += 72
    x_cord = 30
    for i in  range(len(board)):
        color = ""
        if board[i] == W_KING or board[i] == W_KNIGHT:
            color = "white"
        elif board[i] == B_KING or board[i] == B_KNIGHT:
            color = "black"
        gui.text (x_cord, 125, board[i], color, 25)
        x_cord += 72
    gui.update_frame(60)
def is_game_over(board):
    '''
    This functions takes one parameter
    if the king piece of either player is missing
    displays a victory message
    board = list of the 1x9 board (0-8 index)
    '''
    if W_KING not in board:
        print_board(board)
        print ("Black wins!")
        return True
    elif B_KING not in board:
        print_board(board)
        print ("White wins!")
        return True

def move(board, position, direction):
    '''
    This function takes 3 parameters and determines what pieces
    is being refrenced and the direction it will move
    board = list of the 1x9 board (0-8 index)
    position = the validated index refrencing the piece
    direction = the direction the piece will move
    '''
    if board[position] == B_KNIGHT or board[position] == W_KNIGHT:
        move_knight(board, position, direction)
    elif board[position] == W_KING or board[position] == B_KING:
        move_king(board, position, direction)


def main():

    # Create the canvas
    gui = graphics(700, 200, '1 Dimensional Chess')

    # This is the starting board.
    # This board variable can and should be passed to other functions
    # and changed as moves are made.
    board = [W_KING, W_KNIGHT, W_KNIGHT, EMPTY, EMPTY, EMPTY, B_KNIGHT, B_KNIGHT, B_KING]

    # White typically starts in chess.
    # This will change between WHITE and BLACK as the turns progress.
    player = WHITE

    # This variable will be updated to be True if the game is over.
    # The game is over after one of the kings dies.
    is_game_won = False

    # This loop controls the repetitive nature of the turns of the game.
    while not is_game_won:

        print_board(board)

        # Draw the board
        draw_board(board, gui)

        position = int(input(player + ' enter index:\n'))
        direction = input(player + ' enter direction (l or r):\n')

        # If the desired move is valid, then call the move function.
        # Also, change the player variable.
        if is_valid_move(board, position, player):
            if player == WHITE:
                move(board, position, direction)
                player = BLACK
            else:
                move(board, position, direction)
                player = WHITE
            is_game_won = is_game_over(board)
        draw_board(board, gui)

main()