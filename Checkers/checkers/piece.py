"""
Piece and King classes for Checkers game pieces.
"""

import pygame
from .constants import GREY_BORDER, SQUARE_SIZE, CROWN, WHITE
from .abstract_classes import AbstractPiece

class Piece(AbstractPiece):
    """Represents a standard Checkers piece."""
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        """Initialize the Piece instance."""
        self._row = row
        self._col = col
        self._color = color
        self._king = False

        self._x = 0
        self._y = 0
        self.calculate_position()

    def calculate_position(self):
        """Calculate the screen position of the piece."""
        self._x = SQUARE_SIZE * self._col + SQUARE_SIZE // 2
        self._y = SQUARE_SIZE * self._row + SQUARE_SIZE // 2

    def draw(self, win):
        """Draw the piece on the board."""
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY_BORDER, (self._x, self._y), radius + self.OUTLINE)
        pygame.draw.circle(win, self._color, (self._x, self._y), radius)

    def move(self, row, col):
        """Move the piece to a new position."""
        self._row = row
        self._col = col
        self.calculate_position()

    def __repr__(self):
        """Return a string representation of the piece."""
        return str(self.color)
    
    # Getter and Setter for row
    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, value):
        self._row = value
        self.calculate_position()

    # Getter and Setter for col
    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, value):
        self._col = value
        self.calculate_position()

    # Getter for color
    @property
    def color(self):
        return self._color

    # Getter and Setter for king
    @property
    def king(self):
        return self._king

    @king.setter
    def king(self, value):
        self._king = value
    
    # inheritance
class King(Piece):
    """Represents a king piece in Checkers."""
    def __init__(self, row, col, color):
        """Initialize the king piece instance."""
        self.grey_kings = self.white_kings = 0
        super().__init__(row, col, color)
        self.king = True
        if self.color == WHITE:
            self.white_kings += 1
        else:
            self.grey_kings += 1
    
    # polymorphism
    def draw(self, win):
        """Draw the king piece on the board."""
        super().draw(win)
        win.blit(CROWN, (self._x - CROWN.get_width() // 2, self._y - CROWN.get_height() // 2))