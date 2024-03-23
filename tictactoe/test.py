from curses.ascii import EM
from re import L
from tictactoe import *
import numpy as np

def printBoard(board):
    print(np.matrix(board))

# X wins
board1 = [
    [X, X, X],
    [O, O, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]
print("Board 1:")
printBoard(board1)
print("Expected utility: 1, Actual utility:", utility(board1))
print()

board2 = [
    [O, O, EMPTY],
    [X, X, X],
    [EMPTY, EMPTY, EMPTY]
]
print("Board 2:")
printBoard(board2)
print("Expected utility: 1, Actual utility:", utility(board2))
print()

board3 = [
    [O, O, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [X, X, X]
]
print("Board 3:")
printBoard(board3)
print("Expected utility: 1, Actual utility:", utility(board3))
print()

board4 = [
    [X, O, O],
    [X, O, EMPTY],
    [X, EMPTY, EMPTY]
]
print("Board 4:")
printBoard(board4)
print("Expected utility: 1, Actual utility:", utility(board4))
print()

board5 = [
    [O, X, O],
    [EMPTY, X, EMPTY],
    [EMPTY, X, O]
]
print("Board 5:")
printBoard(board5)
print("Expected utility: 1, Actual utility:", utility(board5))
print()

board6 = [
    [O, EMPTY, X],
    [O, EMPTY, X],
    [EMPTY, O, X]
]
print("Board 6:")
printBoard(board6)
print("Expected utility: 1, Actual utility:", utility(board6))
print()

board7 = [
    [X, O, EMPTY],
    [O, X, EMPTY],
    [EMPTY, O, X]
]
print("Board 7:")
printBoard(board7)
print("Expected utility: 1, Actual utility:", utility(board7))
print()

board8 = [
    [EMPTY, O, X],
    [O, X, EMPTY],
    [X, O, EMPTY]
]
print("Board 8:")
printBoard(board8)
print("Expected utility: 1, Actual utility:", utility(board8))
print()

# O wins
board9 = [
    [O, O, O],
    [X, X, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]
print("Board 9:")
printBoard(board9)
print("Expected utility: -1, Actual utility:", utility(board9))
print()

board10 = [
    [X, X, EMPTY], 
    [O, O, O],
    [EMPTY, X, EMPTY]
]
print("Board 10:")
printBoard(board10)
print("Expected utility: -1, Actual utility:", utility(board10))
print()

board11 = [
    [X, EMPTY, EMPTY],
    [X, EMPTY, EMPTY],
    [O, O, O]
]
print("Board 11:")
printBoard(board11)
print("Expected utility: -1, Actual utility:", utility(board11))
print()

board12 = [
    [O, X, X],
    [O, X, EMPTY], 
    [O, EMPTY, X]
]
print("Board 12:")
printBoard(board12)
print("Expected utility: -1, Actual utility:", utility(board12))
print()

# Tie
board13 = [
    [X, O, X],
    [X, O, O],
    [O, X, X]
]
print("Board 13:")
printBoard(board13)
print("Expected utility: 0, Actual utility:", utility(board13))
print()

# Hasn't ended
board14 = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]
print("Board 14:")
printBoard(board14)
print("Expected utility: 0, Actual utility:", utility(board14))
print()

board15 = [
    [X, O, X],
    [X, EMPTY, O],
    [O, EMPTY, EMPTY]
]
print("Board 15:")
printBoard(board15) 
print("Expected utility: 0, Actual utility:", utility(board15))