from ai import AI


class HumanAI(AI):
    """
    Inherits from AI and implements a human player class.
    Methods implemented:
    getNextMove(board, letter) -> Returns next position of placement of the letter by the player
    getName() -> Return the name of the player
    setName(name) -> Set the name of the player as You
    """
    name = "You"

    def setName(self, name):
        """
        Set the name of the player as You
        """
        self.name = name

    def getName(self):
        """
        Returns the name of the player
        """
        return self.name

    def getNextMove(self, board, letter):
        """
        Returns the next position of placement of the letter for the player
        """
        while True:
            move = int(raw_input("Enter the position for your move [1-9]: "))
            if move < 1 or move > 9:
                print "Not a valid move"
            else:
                if board.isSpaceFree(move - 1):
                    return move - 1
                else:
                    print "Not a valid move"
        return None
