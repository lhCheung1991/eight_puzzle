
from eight_puzzle import *

if __name__ == "__main__":
    pass
    # process_file("10_moves.txt", "BFS")
    # process_file("10_moves.txt", "Greedy", 1)
    # process_file("10_moves.txt", "A*", 2)
    # process_file('10_moves.txt', 'DFS', 5)

    eight_puzzle("631074852", "random")    # search the state space randomly
    eight_puzzle("631074852", "BFS")    # BFS searching
    eight_puzzle("631074852", "DFS")    # DFS searching without limit
    eight_puzzle("631074852", "DFS", 25)    # DFS searching with depth-limit 25
    eight_puzzle("631074852", "Greedy")    # Greedy Searching with misplace piles heuristic function
    eight_puzzle("631074852", "Greedy", 1)    # Greedy Searching with Manhattan Distance heuristic function
    eight_puzzle("631074852", "Greedy", 2)    # Greedy Searching with Permutation Inversions heuristic function
    eight_puzzle("631074852", "A*")    # A* Searching with misplace piles heuristic function
    eight_puzzle("631074852", "A*", 1)    # A* Searching with Manhattan Distance heuristic function
    eight_puzzle("631074852", "A*", 2)    # A* Searching with Permutation Inversions heuristic function