#
# searcher.py
#
# classes for objects that perform state-space search on Eight Puzzles
#
# name: 
# email:

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """

    def __init__(self, init_state, depth_limit):
        """

        :param init_state:
        :param depth_limit:
        :return:
        """
        self.states = []    # list of untested states
        self.states.append(init_state)
        self.num_tested = 0    # keep track of how many states the Searcher tests
        self.depth_limit = depth_limit    # how deep in the state-space search tree the Searcher will go

    def should_add(self, state):
        """
        takes a State object called state and returns True if the called Searcher
        should add state to its list of untested states, and False otherwise.
        :param state:
        :return:
        """
        if state.creates_cycle():
            return False
        else:

            if self.depth_limit == -1:
                return True
            else:
                if state.num_moves <= self.depth_limit:
                    return True
                else:
                    return False

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        s = str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


### Add your other class definitions below. ###


