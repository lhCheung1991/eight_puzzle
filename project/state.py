#
# state.py
#
# A State class for the Eight Puzzle
#
# name: 
# email:
#

from board import *

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]]

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']


class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Add your method definitions here. ###

    def __init__(self, board, predecessor, move):
        """

        :param board: reference to the Board object associated with this state
        :param predecessor:  a reference to the State object that comes before this state
        :param move: a string representing the move that was needed to transition
                    from the predecessor state to this state
        :return:
        """
        self.board = board
        self.predecessor = predecessor
        self.move = move

        if predecessor is None:
            self.num_moves = 0    # # of moves from the initial state to this state
        else:
            self.num_moves = predecessor.num_moves + 1

    def is_goal(self):
        """

        :return:
        """
        return self.board.tiles == GOAL_TILES

    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True
    
