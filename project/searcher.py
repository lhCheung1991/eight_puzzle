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

    def add_state(self, new_state):
        self.states.append(new_state)

    def add_states(self, new_states):
        for state in new_states:
            if self.should_add(state):
                self.add_state(state)

    def next_state(self):
        """ chooses the next state to be tested from the list of
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s

    def find_solution(self):

        while len(self.states) > 0:
            curState = self.next_state()
            self.num_tested += 1
            if curState.is_goal():
                return curState
            else:
                self.add_states(curState.generate_successors())
        return None

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


class BFSearcher(Searcher):
    """
    BFSearcher for searcher objects that perform breadth-first search (BFS)
    """
    def next_state(self):
        """
        override the Searcher's next_state()
        :return:
        """
        nextState = self.states.pop(0)
        return nextState


class DFSearcher(Searcher):
    """
    DFSearcher for searcher objects that perform depth-first search (DFS)
    """
    def next_state(self):
        """
        override the Searcher's next_state()
        :return:
        """
        nextState = self.states.pop(-1)
        return nextState


class GreedySearcher(Searcher):
    """
    perform greedy search, uses a heuristic function to estimate the remaining cost
    needed to get from a given state to the goal state
    """

    def __init__(self, init_state, heuristic, depth_limit):
        """ constructor for a GreedySearcher object
            inputs:
             * init_state - a State object for the initial state
             * heuristic - an integer specifying which heuristic
                            function should be used when computing the priority of a state
             * depth_limit - the depth limit of the searcher
        """
        self.heuristic = heuristic
        self.states = [[self.priority(init_state), init_state]]    # sublist is a [priority, state] pair
        self.num_tested = 0
        self.depth_limit = depth_limit

    def priority(self, state):

        priority = 0

        if self.heuristic == 1:    # Manhattan distance
            priority = -1 * state.board.num_manhattanDistance()
        elif self.heuristic == 2:    # permutation inversions
            priority = -1 * state.board.num_permutationInversions()
        else:
            priority = -1 * state.board.num_misplaced()

        return priority

    def add_state(self, state):
        """

        :param state:
        :return:
        """
        self.states.append([self.priority(state), state])

    def next_state(self):
        """

        :return:
        """
        highestPriority = max(self.states)
        nextState = highestPriority[1]
        self.states.remove(highestPriority)
        return nextState


class AStarSearcher(GreedySearcher):
    """
    perform A* search, when A* assigns a priority to a state, it also takes into account the cost
    that has already been expended to get to that state
    """
    def priority(self, state):
        """

        :param state:
        :return:
        """
        priority = 0

        if self.heuristic == 1:
            priority = -1 * (state.board.num_manhattanDistance() + state.num_moves)
        elif self.heuristic == 2:
            priority = -1 * (state.board.num_permutationInversions() + state.num_moves)
        else:
            priority = -1 * (state.board.num_misplaced() + state.num_moves)

        return priority