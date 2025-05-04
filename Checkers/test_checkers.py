import unittest
from main import WIN
from checkers.game import Game
from checkers.constants import WHITE, GREY_PIECES

class TestCheckersGame(unittest.TestCase):
    def setUp(self):
        """Set up the game for testing."""
        self.game = Game(WIN)

    def test_initialization(self):
        """Test the initial state of the game."""
        self.assertEqual(self.game.turn, GREY_PIECES)
        self.assertEqual(len(self.game.board.get_all_pieces(WHITE)), 12)
        self.assertEqual(len(self.game.board.get_all_pieces(GREY_PIECES)), 12)

    def test_select_piece(self):
        """Test selecting a piece."""
        selected_piece = self.game.board.get_piece(2, 1)
        self.assertEqual(selected_piece.row, 2)
        self.assertEqual(selected_piece.col, 1)

    def test_move_piece(self):
        """Test moving a piece."""
        selected_piece = self.game.board.get_piece(5, 0)
        selected_piece = self.game.board.get_piece(5, 0)
        self.assertEqual(selected_piece.row, 5)
        self.assertEqual(selected_piece.col, 0)
        self.game.board.move(selected_piece, 4, 1)
        moved_piece = self.game.board.get_piece(4, 1)
        self.assertEqual(moved_piece.row, 4)
        self.assertEqual(moved_piece.col, 1)
        self.assertEqual(moved_piece.color, GREY_PIECES)

if __name__ == '__main__':
    unittest.main()