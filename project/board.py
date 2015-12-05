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
            curRow = int(idx / 3)
            curCol = int(idx % 3)
            self.tiles[curRow][curCol] = int(val)
            if int(val) == 0:
                self.blank_r = curRow
                self.blank_c = curCol

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

    def move_blank(self, direction):
        """
        :param direction: "up", "down", "left", "right"
        :return: True / False
        """
        if direction not in ["up", "down", "left", "right"]:
            print("unknown direction:" + " " + direction)
            return False

        tmpMovedRow = 0
        tmpMovedCol = 0

        if direction == "up":
            tmpMovedRow = self.blank_r - 1
            tmpMovedCol = self.blank_c
        elif direction == "down":
            tmpMovedRow = self.blank_r + 1
            tmpMovedCol = self.blank_c
        elif direction == "left":
            tmpMovedRow = self.blank_r
            tmpMovedCol = self.blank_c - 1
        elif direction == "right":
            tmpMovedRow = self.blank_r
            tmpMovedCol = self.blank_c + 1

        if tmpMovedRow >= 0 and tmpMovedRow <= 2 and tmpMovedCol >= 0 and tmpMovedCol <= 2:
            self.tiles[self.blank_r][self.blank_c] = self.tiles[tmpMovedRow][tmpMovedCol]
            self.tiles[tmpMovedRow][tmpMovedCol] = 0
            self.blank_r = tmpMovedRow
            self.blank_c = tmpMovedCol
            return True
        else:
            return False

    def digit_string(self):
        ansStr = ""
        for lst in self.tiles:
            for digit in lst:
                ansStr += str(digit)
        return ansStr

    def copy(self):
        return Board(self.digit_string())

    def num_misplaced(self):
        """
        counts and returns the number of tiles in the called Board object
        that are not where they should be in the goal state
        :return:
        """
        misPlacedCount = 0
        for idx in range(9):
            tmpRow = idx / 3
            tmpCol = idx % 3

            if self.tiles[tmpRow][tmpCol] != 0 and self.tiles[tmpRow][tmpCol] != idx:
                misPlacedCount += 1

        return misPlacedCount

    def __eq__(self, other):
        return self.tiles == other.tiles