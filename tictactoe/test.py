from curses.ascii import EM
from re import L
from tictactoe import *
import numpy as np

def printBoard(board):
    print(np.matrix(board))


board = [
    [X, O, O],
    [O, X, X],
    [X, O, O]
]
print(utility(board))