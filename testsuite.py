import unittest
from board import Board
from pseudorandomai import PseudoRandomAI


class TestBoard(unittest.TestCase):
    """
    Test suit to test the board class.
    Test cases implemented:
    testEmptyBoard -> Tests if the board is empty
    testIsSpaceFree -> Tests if the given space is free on the board
    testWinner -> Tests if the player with the specified letter has won
    testInvalidMove -> Tests if the specified move is invalid
    testBoardFull -> Tests if the board is full
    """
    def testEmptyBoard(self):
        """
        Tests if the board is empty
        """
        board = Board()
        self.assertEqual(board.isEmpty(), True)
        board.makeMove(0, 'X')
        self.assertEqual(board.isEmpty(), False)

    def testIsSpaceFree(self):
        """
        Tests if the given space is free on the board
        """
        board = Board()
        board.makeMove(5, 'O')
        self.assertEqual(board.isSpaceFree(5), False)

    def testWinner(self):
        """
        Tests if the player with the specified letter has won the board
        """
        board = Board()
        board.makeMove(0, 'X')
        board.makeMove(1, 'X')
        board.makeMove(2, 'X')
        self.assertEqual(board.isWinner('X'), True)

    def testInvalidMove(self):
        """
        Tests if the specified move is invalid
        """
        board = Board()
        board.makeMove(0, 'X')
        self.assertEqual(board.makeMove(0, 'X'), False)

    def testBoardFull(self):
        """
        Tests if the board is full
        """
        board = Board()
        for i in range(9):
            board.makeMove(i, 'X')
        self.assertEqual(board.isFull(), True)


class TestAI(unittest.TestCase):
    """
    Test suit to test the Pseudorandom AI.
    Test cases implemented:
    testNextMove -> Tests the next move returned by the AI
    testNoMove -> Tests if the getNextMove returns None if all the spaces are filled
    """
    def testNextMove(self):
        """
        Tests the next move returned by the AI
        """
        ai = PseudoRandomAI()
        # If corners are free, choose the corners
        board = Board()
        self.assertIn(ai.getNextMove(board, 'X'), [0, 2, 6, 8])
        board.makeMove(0, 'X')
        board.makeMove(1, 'O')
        board.makeMove(2, 'X')
        board.makeMove(6, 'O')
        self.assertEqual(ai.getNextMove(board, 'X'), 8)
        # If corners, aren't free, choose the center if free
        board.makeMove(8, 'X')
        self.assertEqual(ai.getNextMove(board, 'X'), 4)
        # If center is not free, choose any other
        board.makeMove(4, 'O')
        self.assertIn(ai.getNextMove(board, 'X'), [1, 3, 5, 7])


    def testNoMove(self):
        """
        Tests if the getNextMove returns None if all the spaces are filled
        """
        ai = PseudoRandomAI()
        board = Board()
        board.makeMove(0, 'X')
        board.makeMove(1, 'O')
        board.makeMove(2, 'X')
        board.makeMove(3, 'O')
        board.makeMove(4, 'X')
        board.makeMove(5, 'O')
        board.makeMove(6, 'X')
        board.makeMove(7, 'O')
        board.makeMove(8, 'X')
        self.assertEqual(ai.getNextMove(board, 'X'), None)

