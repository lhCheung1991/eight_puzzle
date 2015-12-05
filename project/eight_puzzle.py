#
# eight_puzzle.py
#
# driver/test code for state-space search on Eight Puzzles
#
# name: 
# email:
#
#

from searcher import *
from timer import *

def create_searcher(init_state, algorithm, extra):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * init_state - a State object for the searcher's initial state
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * extra - an optional extra parameter that can be used to
            specify either a depth limit or the number of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(init_state, extra)
## You will uncommment the following lines as you implement
## other algorithms.
    #elif algorithm == 'BFS':
    #    searcher = BFSearcher(init_state, extra)
    #elif algorithm == 'DFS':
    #    searcher = DFSearcher(init_state, extra)
    #elif algorithm == 'Greedy':
    #    searcher = GreedySearcher(init_state, extra, -1)
    #elif algorithm == 'A*':
    #    searcher = AStarSearcher(init_state, extra, -1)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher


def eight_puzzle(init_boardstr, algorithm, extra=-1):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * extra - an optional extra parameter that can be used to
            specify either a depth limit or the number of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')

    searcher = create_searcher(init_state, algorithm, extra)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution()
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()
