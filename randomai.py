import random
from ai import AI


class RandomAI(AI):
    """
    Inherits from AI and implements a random AI.
    Methods implemented:
    getNextMove(board, letter) -> Returns next position of placement of the letter by the AI
    chooseRandomFromList(board, list) -> Return a valid move using a random choice
    getName() -> Return the name of the AI
    """

    def getNextMove(self, board, letter):
        """
        Returns the next position of placement of the letter for the AI
        """
        return self.chooseRandomMoveFromList(board, range(9))


    def chooseRandomMoveFromList(self, board, movesList):
        """
        Returns a valid move from the passed list on the passed board.
        Returns None if there is no valid move.
        """
        possibleMoves = []
        for i in movesList:
            if board.isSpaceFree(i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None


    def getName(self):
        """
        Returns the name of the AI
        """
        return "Random AI"
