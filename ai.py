from abc import ABCMeta, abstractmethod


class AI:
    """
    Abstract base class for AI
    Virtual methods implemented:
    getNextMove(board, letter)
    getName()
    """

    @abstractmethod
    def getNextMove(self, board, letter):
        """
        Returns the next position of placement of the letter for the player
        """

    @abstractmethod
    def getName(self):
        """
        Returns the name of the AI
        """
