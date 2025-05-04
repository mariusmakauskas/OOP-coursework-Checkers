"""
Board class for managing the Checkers game board.
"""

import pygame
from .constants import BLACK, ROWS, GREY_PIECES, SQUARE_SIZE, COLS, WHITE
from .piece import Piece, King
from .abstract_classes import AbstractBoard

class Board(AbstractBoard):
    """Represents the Checkers game board."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Ensure only one instance of the Game class is created (Singleton pattern)."""
        if cls._instance is None:
            cls._instance = super(Board, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize the Board."""
        if not hasattr(self, "_initialized"):
            self._board = []
            self._selected_piece = None
            self._grey_left = 12
            self._white_left = 12
            self.create_board()
            self._winner_declared = False
            self._initialized = True

    def get_all_pieces(self, color):
        """Get all pieces of a specific color on the board."""
        pieces = []
        for row in self._board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def draw_squares(self, win):
        """Draw the squares of the board."""
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(
                    win, 
                    WHITE, 
                    (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                )

    def move(self, piece, row, col):
        """Move a piece to a new position."""
        self._board[piece.row][piece.col], self._board[row][col] = (
            self._board[row][col], 
            self._board[piece.row][piece.col]
        )
        piece.move(row, col)
        if row == ROWS - 1 or row == 0:
            self.board[row][col] = King(row, col, piece.color)
            

    def get_piece(self, row, col):
        """Get the piece at a specific position."""
        return self._board[row][col]

    def create_board(self):
        """Create the initial board setup."""
        for row in range(ROWS):
            self._board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self._board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self._board[row].append(Piece(row, col, GREY_PIECES))
                    else:
                        self._board[row].append(0)
                else:
                    self._board[row].append(0)

    def draw(self, win):
        """Draw the board and all pieces."""
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self._board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):
        """Remove pieces from the board."""
        for piece in pieces:
            self._board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == GREY_PIECES:
                    self._grey_left -= 1
                else:
                    self._white_left -= 1

    def winner(self):
        """Determine the winner of the game."""
        if self.winner_declared:
            return None
        if self.grey_left <= 0:
            self.winner_declared = True
            return print("WHITE")
        elif self.white_left <= 0:
            self.winner_declared = True
            return print("GREY")

        return None

    def get_valid_moves(self, piece):
        """Get all valid moves for a given piece."""
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        
        if piece.color == GREY_PIECES or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))

        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves
        
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        """Helper function to check left diagonals for valid moves."""
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0: # Stop if out of bounds
                break

            current = self._board[r][left]
            if current == 0: # Empty square
                if skipped and not last: # If there are skipped pieces but no piece to jump over
                    break
                elif skipped: # Valid jump
                    moves[(r, left)] = last + skipped
                else: # Regular move
                    moves[(r, left)] = last

                if last: # Continue checking for further jumps
                    row = -1 if step == -1 else ROWS
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break

            elif current.color == color: # Same color, stop
                break
            else: # Opponent's piece
                last = [current]

            left -= 1

        return moves


    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        """Helper function to check right diagonals for valid moves."""
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS: # Stop if out of bounds
                break

            current = self._board[r][right]
            if current == 0: # Empty square
                if skipped and not last: # If there are skipped pieces but no piece to jump over
                    break
                elif skipped: # Valid jump
                    moves[(r, right)] = last + skipped
                else: # Regular move
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break

            elif current.color == color: # Same color, stop
                break
            else: # Opponent's piece
                last = [current]

            right += 1

        return moves
    
    # Getter for board
    @property
    def board(self):
        return self._board

    # Getter and Setter for selected_piece
    @property
    def selected_piece(self):
        return self._selected_piece

    @selected_piece.setter
    def selected_piece(self, piece):
        self._selected_piece = piece

    # Getter for grey_left
    @property
    def grey_left(self):
        return self._grey_left

    # Getter for white_left
    @property
    def white_left(self):
        return self._white_left

    # Getter and Setter for winner_declared
    @property
    def winner_declared(self):
        return self._winner_declared

    @winner_declared.setter
    def winner_declared(self, value):
        self._winner_declared = value