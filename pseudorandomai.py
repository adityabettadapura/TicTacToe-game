import random
from ai import AI


class PseudoRandomAI(AI):
    """
    Inherits from AI and implements a random AI.
    Methods implemented:
    getNextMove(board, letter) -> Returns next position of placement of the letter by the AI
    chooseRandomFromList(board, list) -> Return a valid move using a random choice
    getName() -> Return the name of the AI
    """
    def getName(self):
        """
        Return name of the AI
        """
        return "Pseudo Random AI"

    def getNextMove(self, board, letter):
        """
        Returns next position of placement of the letter by the AI
        """
        if letter == 'X':
            opponentLetter = 'O'
        else:
            opponentLetter = 'X'

        # First, check if we can win in the next move
        for i in range(9):
            copy = board.getBoard()
            if copy.isSpaceFree(i):
                copy.makeMove(i, letter)
                if copy.isWinner(letter):
                    return i

        # Check if the player could win on their next move, and block them.
        for i in range(9):
            copy = board.getBoard()
            if copy.isSpaceFree(i):
                copy.makeMove(i, opponentLetter)
                if copy.isWinner(opponentLetter):
                    return i

        # Try to take one of the corners, if they are free.
        move = self.chooseRandomMoveFromList(board, [0, 2, 6, 8])
        if move != None:
            return move

        # Try to take the center, if it is free.
        if board.isSpaceFree(4):
            return 4

        # Move on one of the sides.
        return self.chooseRandomMoveFromList(board, [1, 3, 5, 7])

    def chooseRandomMoveFromList(self, board, movesList):
        """
        Return a valid move using a random choice
        """
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if board.isSpaceFree(i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None
