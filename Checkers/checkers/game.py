"""Game class for managing the Checkers game logic."""

import pygame
from .constants import WHITE, GREY_PIECES, BLUE, SQUARE_SIZE
from .board import Board
from .abstract_classes import AbstractGame

class Game(AbstractGame):
    """Manages the Checkers game logic, including moves, turns, and logging."""
    _instance = None  # Class-level attribute to hold the single instance

    def __new__(cls, *args, **kwargs):
        """Ensure only one instance of the Game class is created (Singleton pattern)."""
        if cls._instance is None:
            cls._instance = super(Game, cls).__new__(cls)
        return cls._instance

    def __init__(self, win):
        """Initialize the Game instance."""
        if not hasattr(self, "_initialized"):
            self._init()
            self._win = win
            self._log_file = "game_log.txt"
            self._clear_log()
            self._initialized = True

    def _init(self): # Needed when resetting only certain attributes
        """Initialize the game state."""
        self._selected_piece = None
        self._board = Board()
        self._turn = GREY_PIECES
        self.valid_moves = {}

    def _clear_log(self):
        """Clear the log file at the start of the game."""
        with open(self._log_file, "w") as file:
            file.write("Game Log\n")
            file.write("=========\n")

    def _get_color_name(self, color):
        """Map RGB color to its name."""
        if color == GREY_PIECES:
            return "GREY"
        elif color == WHITE:
            return "WHITE"
        return "UNKNOWN"

    def _log_move(self, piece, start_pos, end_pos):
        """Log a move to the file."""
        color_name = self._get_color_name(piece.color)
        with open(self._log_file, "a") as file:
            file.write(f"Move: {color_name} from {start_pos} to {end_pos}\n")

    def _log_removed_pieces(self, removed_pieces):
        """Log removed pieces to the file."""
        with open(self._log_file, "a") as file:
            for piece in removed_pieces:
                color_name = self._get_color_name(piece.color)
                file.write(f"Removed: {color_name} at ({piece.row}, {piece.col})\n")

    def update(self):
        """Update the game state and redraw the board."""
        self._board.draw(self._win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def winner(self):
        """Determine the winner of the game."""
        return self._board.winner()

    def reset(self):
        """Reset the game state to its initial configuration."""
        self._init()

    def select(self, row, col):
        """Select a piece."""
        if self._selected_piece:
            result = self._move(row, col)
            if not result:
                self._selected_piece = None
                self.select(row, col)
        piece = self._board.get_piece(row, col)
        if piece != 0 and piece.color == self._turn:
            self._selected_piece = piece
            self.valid_moves = self._board.get_valid_moves(piece)
            return True
        return False

    def _move(self, row, col):
        """Move a piece to a new position."""
        piece = self._board.get_piece(row, col)
        if self._selected_piece and piece == 0 and (row, col) in self.valid_moves:
            start_pos = (self._selected_piece.row, self._selected_piece.col)
            self._board.move(self._selected_piece, row, col)
            end_pos = (row, col)
            self._log_move(self._selected_piece, start_pos, end_pos)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self._board.remove(skipped)
                self._log_removed_pieces(skipped)
            self.change_turn()
        else:
            return False
        return True
            
    def draw_valid_moves(self, moves):
        """Draw valid moves on the board."""
        for move in moves:
            row, col = move
            pygame.draw.circle(self._win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        """Change the current player's turn."""
        self.valid_moves = {}
        if self._turn == GREY_PIECES:
            self._turn = WHITE
        else:
            self._turn = GREY_PIECES

    # Getter for win
    @property
    def win(self):
        return self._win

    # Setter for win
    @win.setter
    def win(self, value):
        self._win = value

    # Getter and Setter for _selected_piece
    @property
    def selected_piece(self):
        return self._selected_piece

    @selected_piece.setter
    def selected_piece(self, piece):
        self._selected_piece = piece

    # Getter and Setter for _board
    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board

    # Getter and Setter for _turn
    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, turn):
        self._turn = turn