#
# eight_puzzle.py
#
# driver/test code for state-space search on Eight Puzzles
#
# name: 
# email:

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
    elif algorithm == 'BFS':
       searcher = BFSearcher(init_state, extra)
    elif algorithm == 'DFS':
       searcher = DFSearcher(init_state, extra)
    elif algorithm == 'Greedy':
       searcher = GreedySearcher(init_state, extra, -1)
    elif algorithm == 'A*':
       searcher = AStarSearcher(init_state, extra, -1)
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


def process_file(filename, algorithm, extra=-1):
    """

    :param filename:
    :param algorithm:
    :param extra:
    :return:
    """
    try:
        lstPuzzles = []
        with open(filename, "r") as inFile:
            lstPuzzles = inFile.readlines()

        lstPuzzles = [line.strip("\n") for line in lstPuzzles]


        solvedPuzzleCnt = 0
        averMoves = 0
        averTestedMoves = 0
        for puzzle in lstPuzzles:
            initBoard = Board(puzzle)
            initState = State(initBoard, None, "init")

            searcher = create_searcher(initState, algorithm, extra)
            if searcher is None:
                return

            solution = None
            try:
                solution = searcher.find_solution()
            except KeyboardInterrupt:
                # print('Search terminated.')
                pass
                print(puzzle + ": search terminated, no solution")
                continue

            if solution is not None:
                print(puzzle + ": " + str(solution.num_moves) + " moves, " +
                      str(searcher.num_tested) + " states tested")
                solvedPuzzleCnt += 1
                averMoves += solution.num_moves
                averTestedMoves += searcher.num_tested
            else:
                print(puzzle + ": no solution")

        print("")
        print("solved " + str(solvedPuzzleCnt) + " puzzles")
        if solvedPuzzleCnt != 0:
            print("averages: " + str(averMoves / solvedPuzzleCnt) + " moves, " +
                  str(averTestedMoves / solvedPuzzleCnt) + " states tested")

    except FileNotFoundError:
        pass


