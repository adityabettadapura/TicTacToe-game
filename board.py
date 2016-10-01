from copy import deepcopy


class Board:
    """
    This implements the 3x3 grid on which the player will make their moves.
    Methods implemented:
    printBoard() -> This provides the text based user interface and will print the board.
    isSpaceFree(number) -> Checks if a square in the 3x3 grid is free
    makeMove(number, letter) -> Marks a free square according to the letter sent
    getBoard() -> Returns a deepcopy of the board
    isFull -> Checks if the board is full
    isEmpty -> Checks that there is free space when a new board is initialized
    isWinner(letter) -> Checks if a player has won. Checks 3 rows, 3 columns and 2 diagonals
    """
    def __init__(self):
        self.squares = [' '] * 9
        print len(self.squares)

    def printBoard(self):
        """
        This provides the text based user interface and will print the board.
        """
        print ""
        print('   |   |')
        print(' ' + self.squares[0] + ' | ' + self.squares[1] + ' | ' + self.squares[2])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.squares[3] + ' | ' + self.squares[4] + ' | ' + self.squares[5])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.squares[6] + ' | ' + self.squares[7] + ' | ' + self.squares[8])
        print('   |   |')
        print ""

    def isSpaceFree(self, number):
        """
        Checks if a square in the 3x3 grid is free
        """
        return (self.squares[number] == ' ')

    def makeMove(self, number, letter):
        """
        Marks a free square according to the letter sent
        """
        if self.squares[number] == ' ':
            self.squares[number] = letter
            return True
        else:
            return False

    def getBoard(self):
        """
        Returns a deepcopy of the board
        """
        return deepcopy(self)

    def isFull(self):
        """
        Checks if the board is full
        """
        for i in range(9):
            if self.isSpaceFree(i):
                return False
        return True

    def isEmpty(self):
        """
        Checks that there is free space when a new board is initialized
        """
        for i in range(9):
            if not self.isSpaceFree(i):
                return False
        return True

    def isWinner(self, letter):
        """
        Checks if a player has won. Checks 3 rows, 3 columns and 2 diagonals
        """
        return (
            (self.squares[6] == letter and self.squares[7] == letter and self.squares[8] == letter) or  # across the top
            (self.squares[3] == letter and self.squares[4] == letter and self.squares[5] == letter) or  # across the middle
            (self.squares[0] == letter and self.squares[1] == letter and self.squares[
                2] == letter) or  # across the self.squaresttom
            (self.squares[0] == letter and self.squares[3] == letter and self.squares[6] == letter) or  # down the left side
            (self.squares[1] == letter and self.squares[4] == letter and self.squares[7] == letter) or  # down the middle
            (
                self.squares[2] == letter and self.squares[5] == letter and self.squares[8] == letter) or  # down the right side
            (self.squares[0] == letter and self.squares[4] == letter and self.squares[8] == letter) or  # diagonal
            (self.squares[6] == letter and self.squares[4] == letter and self.squares[2] == letter))
