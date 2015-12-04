#
# board.py
#
# A Board class for the Eight Puzzle
#
# name: 
# email:
#
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        for idx, val in enumerate(digitstr):
            curRow = idx / 3
            curCol = idx % 3
            self.tiles[curRow][curCol] = int(val)
            if int(val) == 0:
                self.blank_r = curRow
                self.blank_c = curCol

    ### Add your other method definitions below. ###

    def __repr__(self):
        reprStr = ""

        for lst in self.tiles:

            for digit in lst:

                if digit != 0:
                    reprStr += str(digit)
                    reprStr += " "
                else:
                    reprStr += "_"
                    reprStr += " "

            reprStr += "\n"

        return reprStr
