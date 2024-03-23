"""
Tic Tac Toe Player
"""

from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # count apperance
    countX, countO = 0, 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                countX += 1
            elif board[i][j] == O:
                countO += 1
    
    ans = EMPTY
    # Not terminal board
    if countX + countO < 9:
        if countO >= countX:
            ans = X
        else:
            ans = O

    return ans
        

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ans = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                ans.add((i, j))
    
    return ans


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    ans = deepcopy(board)
    # get the turn's player
    chess = player(ans)
    row, column = action[0], action[1]
    if ans[row][column] == EMPTY:
        # is valid action
        ans[row][column] = chess
        return ans
    else:
        raise ValueError



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # horizontal
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
    # vertical
    for j in range(len(board[0])):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j]:
            return board[0][j]
    # diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[1][1] 
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[1][1]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for i in range(len(board)):
        for j in range(len(board[0])):
            # still in progress
            if board[i][j] is EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # assume terminal(board) is True
    win = winner(board)
    ans = 0
    if win == X:
        ans = 1
    elif win == O:
        ans = -1
    return ans


def pickMax(board, bestScore):
    # Is leaf, no more recursion
    if (terminal(board)):
        return utility(board)

    choices = actions(board)
    maxValue = -10
    for choice in choices:
        maxValue = max(maxValue, pickMin(result(board, choice), maxValue))
        if maxValue > bestScore:
            break
    
    return maxValue


def pickMin(board, bestScore):
    # Is leaf, no more recursion
    if (terminal(board)):
        return utility(board)

    choices = actions(board)
    minValue = 10
    for choice in choices:
        minValue = min(minValue, pickMax(result(board, choice), minValue))
        if minValue < bestScore:
            break
    
    return minValue

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # decide to pick max or min according to the role
    role = player(board)
    choices = actions(board)
    action = None
    if role == X:
        maxScore = -10
        for choice in choices:
            # current score after making the choice
            cur = pickMin(result(board, choice), maxScore)
            if cur > maxScore:
                # record the best choice which can produce maxScore
                maxScore = cur
                action = choice
    elif role == O:
        minScore = 10
        for choice in choices:
            # current score after making the choice
            cur = pickMax(result(board, choice), minScore)
            if cur < minScore:
                # record the best choice which can produce minScore
                minScore = cur
                action = choice
    
    return action


