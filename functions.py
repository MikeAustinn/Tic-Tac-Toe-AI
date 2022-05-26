""" A file for most supporting functions 
    Please add tests for functions added in the testing.py file """

from numpy import array



def print_board(board: array):
    print('\n'.join([''.join([col for col in row])
        for row in board])) # Prints a 2D Array

def take_move(data: array, player: int, move: int):
    """ Get user input, check if valid and update data if True
    Args: Data of board, which players move (1 == 'X', 2 == 'O'),
    Return: Updated board data """
    if data[move-1] == 0:
        data[move-1] = player
    return data

def update():
    """ Update data for game to use 
    Args: Data to update, Board(s) to update
    Return: Updated Board(s) """
    pass

def win_check(board):
    sign = 1
    while sign <= 2:
        return((board[0]== sign and board[1]==  sign and board[2]== sign )or #for row1 

                (board[3]== sign and board[4]== sign and board[5]== sign )or #for row2

                (board[6]== sign and board[7]== sign and board[8]== sign )or #for row3

                (board[0]== sign and board[3]== sign and board[6]==  sign )or#for Colm1 

                (board[1]== sign and board[4]== sign and board[7]== sign )or #for Colm 2

                (board[2]== sign and board[5]== sign and board[8]== sign )or #for colm 3

                (board[0]== sign and board[4]== sign and board[8]== sign )or #daignole 1

                (board[2]== sign and board[4]== sign and board[6]== sign )) #daignole 2

    sign += 1

    return 0

win_check
