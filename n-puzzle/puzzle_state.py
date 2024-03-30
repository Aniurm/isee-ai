from queue import PriorityQueue
import numpy as np
from enum import Enum
import copy


# Enum of operation in EightPuzzle problem
class Move(Enum):
    """
    The class of move operation
    NOTICE: The direction denotes the 'blank' space move
    """
    Up = 0
    Down = 1
    Left = 2
    Right = 3


# EightPuzzle state
class PuzzleState(object):
    """
    Class for state in EightPuzzle-Problem
    Attr:
        square_size: Chessboard size, e.g: In 8-puzzle problem, square_size = 3
        state: 'square_size' x 'square_size square', '-1' indicates the 'blank' block  (For 8-puzzle, state is a 3 x 3 array)
        g: The cost from initial state to current state
        h: The value of heuristic function
        pre_move:  The previous operation to get to current state
        pre_state: Parent state of this state
    """
    def __init__(self, square_size = 3):
        self.square_size = square_size
        self.state = None
        self.g = 0
        self.h = 0
        self.pre_move = None
        self.pre_state = None

        self.generate_state()

    def __eq__(self, other):
        return (self.state == other.state).all()

    def __str__(self):
        return np.array_str(self.state)
    
    def __lt__(self, other):
        # Compare PuzzleState objects based on their f value (g + h)
        return (self.g + self.h) < (other.g + other.h)

    def blank_pos(self):
        """
        Find the 'blank' position of current state
        :return:
            row: 'blank' row index, '-1' indicates the current state may be invalid
            col: 'blank' col index, '-1' indicates the current state may be invalid
        """
        index = np.argwhere(self.state == -1)
        row = -1
        col = -1
        if index.shape[0] == 1:  # find blank
            row = index[0][0]
            col = index[0][1]
        return row, col

    def num_pos(self, num):
        """
        Find the 'num' position of current state
        :return:
            row: 'num' row index, '-1' indicates the current state may be invalid
            col: 'num' col index, '-1' indicates the current state may be invalid
        """
        index = np.argwhere(self.state == num)
        row = -1
        col = -1
        if index.shape[0] == 1:  # find number
            row = index[0][0]
            col = index[0][1]
        return row, col

    def is_valid(self):
        """
        Check current state is valid or not (A valid state should have only one 'blank')
        :return:
            flag: boolean, True - valid state, False - invalid state
        """
        row, col = self.blank_pos()
        if row == -1 or col == -1:
            return False
        else:
            return True

    def clone(self):
        """
        Return the state's deepcopy
        :return:
        """
        return copy.deepcopy(self)

    def generate_state(self, random=False, seed=None):
        """
        Generate a new state
        :param random: True - generate state randomly, False - generate a normal state
        :param seed: Choose the seed of random, only used when random = True
        :return:
        """
        self.state = np.arange(0, self.square_size ** 2).reshape(self.square_size, -1)
        self.state[self.state == 0] = -1  # Set blank

        if random:
            np.random.seed(seed)
            np.random.shuffle(self.state)

    def display(self):
        """
        Print state
        :return:
        """
        print("----------------------")
        for i in range(self.state.shape[0]):
            # print("{}\t{}\t{}\t".format(self.state[i][0], self.state[i][1], self.state[i][2]))
            # print(self.state[i, :])
            for j in range(self.state.shape[1]):
                if j == self.state.shape[1] - 1:
                    print("{}\t".format(self.state[i][j]))
                else:
                    print("{}\t".format(self.state[i][j]), end='')
        print("----------------------\n")


def check_move(curr_state, move):
    """
    Check the operation 'move' can be performed on current state 'curr_state'
    :param curr_state: Current puzzle state
    :param move: Operation to be performed
    :return:
        valid_op: boolean, True - move is valid; False - move is invalid
        src_row: int, current blank row index
        src_col: int, current blank col index
        dst_row: int, future blank row index after move
        dst_col: int, future blank col index after move
    """
    # assert isinstance(move, Move)  # Check operation type
    assert curr_state.is_valid()

    if not isinstance(move, Move):
        move = Move(move)

    src_row, src_col = curr_state.blank_pos()
    dst_row, dst_col = src_row, src_col
    valid_op = False

    if move == Move.Up:  # Number moves up, blank moves down
        dst_row -= 1
    elif move == Move.Down:
        dst_row += 1
    elif move == Move.Left:
        dst_col -= 1
    elif move == Move.Right:
        dst_col += 1
    else:  # Invalid operation
        dst_row = -1
        dst_col = -1

    if dst_row < 0 or dst_row > curr_state.state.shape[0] - 1 or dst_col < 0 or dst_col > curr_state.state.shape[1] - 1:
        valid_op = False
    else:
        valid_op = True

    return valid_op, src_row, src_col, dst_row, dst_col


def once_move(curr_state, move):
    """
    Perform once move to current state
    :param curr_state:
    :param move:
    :return:
        valid_op: boolean, flag of this move is valid or not. True - valid move, False - invalid move
        next_state: EightPuzzleState, state after this move
    """
    valid_op, src_row, src_col, dst_row, dst_col = check_move(curr_state, move)

    next_state = curr_state.clone()

    if valid_op:
        it = next_state.state[dst_row][dst_col]
        next_state.state[dst_row][dst_col] = -1
        next_state.state[src_row][src_col] = it
        next_state.pre_state = curr_state
        next_state.pre_move = move
        return True, next_state
    else:
        return False, next_state


def check_state(src_state, dst_state):
    """
    Check current state is same as destination state
    :param src_state:
    :param dst_state:
    :return:
    """
    return (src_state.state == dst_state.state).all()


def run_moves(curr_state, dst_state, moves):
    """
    Perform list of move to current state, and check the final state is same as destination state or not
    Ideally, after we perform moves to current state, we will get a state same as the 'dst_state'
    :param curr_state: EightPuzzleState, current state
    :param dst_state: EightPuzzleState, destination state
    :param moves: List of Move
    :return:
        flag of moves: True - We can get 'dst_state' from 'curr_state' by 'moves'
    """
    pre_state = curr_state.clone()
    next_state = None

    for move in moves:
        valid_move, next_state = once_move(pre_state, move)

        if not valid_move:
            return False

        pre_state = next_state.clone()

    if check_state(next_state, dst_state):
        return True
    else:
        return False


def runs(curr_state, moves):
    """
    Perform list of move to current state, get the result state
    NOTICE: The invalid move operation would be ignored
    :param curr_state:
    :param moves:
    :return:
    """
    pre_state = curr_state.clone()
    next_state = None

    for move in moves:
        valid_move, next_state = once_move(pre_state, move)
        pre_state = next_state.clone()
    return next_state


def print_moves(init_state, moves):
    """
    While performing the list of move to current state, this function will also print how each move is performed
    :param init_state: The initial state
    :param moves: List of move
    :return:
    """
    print("Initial state")
    init_state.display()

    pre_state = init_state.clone()
    next_state = None

    for idx, move in enumerate(moves):
        if move == Move.Up:  # Number moves up, blank moves down
            print("{} th move. Goes up.".format(idx))
        elif move == Move.Down:
            print("{} th move. Goes down.".format(idx))
        elif move == Move.Left:
            print("{} th move. Goes left.".format(idx))
        elif move == Move.Right:
            print("{} th move. Goes right.".format(idx))
        else:  # Invalid operation
            print("{} th move. Invalid move: {}".format(idx, move))

        valid_move, next_state = once_move(pre_state, move)

        if not valid_move:
            print("Invalid move: {}, ignore".format(move))

        next_state.display()

        pre_state = next_state.clone()

    print("We get final state: ")
    next_state.display()


def generate_moves(move_num = 30):
    """
    Generate a list of move in a determined length randomly
    :param move_num:
    :return:
        move_list: list of move
    """
    move_dict = {}
    move_dict[0] = Move.Up
    move_dict[1] = Move.Down
    move_dict[2] = Move.Left
    move_dict[3] = Move.Right

    index_arr = np.random.randint(0, 4, move_num)
    index_list = list(index_arr)

    move_list = [move_dict[idx] for idx in index_list]

    return move_list


def convert_moves(moves):
    """
    Convert moves from int into Move type
    :param moves:
    :return:
    """
    if len(moves):
        if isinstance(moves[0], Move):
            return moves
        else:
            return [Move(move) for move in moves]
    else:
        return moves


def update_cost(curr_state, dst_state):
    """
    Update the cost of the current state (g and h values).
    """
    def manhattan_distance(state1, state2):
        total_dist = 0
        for i in range(1, state1.square_size ** 2):
            x1, y1 = state1.num_pos(i)
            x2, y2 = state2.num_pos(i)
            total_dist += abs(x1 - x2) + abs(y1 - y2)
        return total_dist

    curr_state.g = curr_state.g if curr_state.pre_state is None else curr_state.pre_state.g + 1
    curr_state.h = manhattan_distance(curr_state, dst_state)

def astar_search_for_puzzle_problem(init_state, dst_state):
    # Initialize the open list with the initial state
    open_list = PriorityQueue()
    open_list.put((0, init_state))

    # Dictionary to store the best g values for visited states
    visited = {str(init_state): init_state.g}

    while not open_list.empty():
        # Get the state with the lowest f value
        _, curr_state = open_list.get()

        # Check if we reached the destination state
        if check_state(curr_state, dst_state):
            # Reconstruct the path
            path = []
            while curr_state.pre_move is not None:
                path.append(curr_state.pre_move)
                curr_state = curr_state.pre_state
            return path[::-1]  # Return reversed path

        # Iterate over possible moves
        for move in Move:
            valid_move, next_state = once_move(curr_state, move)
            if valid_move:
                update_cost(next_state, dst_state)
                f_value = next_state.g + next_state.h
                next_state_str = str(next_state)

                # Check if this path is better than any previously found path
                if next_state_str not in visited or f_value < visited[next_state_str]:
                    visited[next_state_str] = f_value
                    open_list.put((f_value, next_state))

    return []  # Return empty list if no path is found
