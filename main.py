""" Main file to be run and play game in terminal so far """
from functions import print_board
from functions import take_move

visual_board = [[' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
                ['_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_'],
                [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
                ['_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_'],
                [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ']]

data_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]



def main() -> None:

    data_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    visual_board = [[' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
                ['_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_'],
                [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
                ['_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_'],
                [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ']]

    print_board(visual_board)
    take_move()

    pass

if __name__ == "__main__":
    main()
