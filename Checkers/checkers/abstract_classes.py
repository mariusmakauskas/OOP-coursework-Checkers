"""
Abstract classes for the Checkers game.
"""

from abc import ABC, abstractmethod

class AbstractBoard(ABC):
    """Abstract class for the Checkers game board."""
    @abstractmethod
    def move(self, piece, row, col):
        """Move a piece to a new position."""
        pass

    @abstractmethod
    def draw(self, win):
        """Draw the board and its pieces."""
        pass

    @abstractmethod
    def get_valid_moves(self, piece):
        """Get all valid moves for a given piece."""
        pass

class AbstractGame(ABC):
    """Abstract class for the Checkers game logic."""
    @abstractmethod
    def select(self, row, col):
        """Select a piece or make a move."""
        pass

    @abstractmethod
    def update(self):
        """Update the game state and redraw the board."""
        pass

    @abstractmethod
    def winner(self):
        """Determine the winner of the game."""
        pass

class AbstractPiece(ABC):
    """Abstract class for a Checkers game piece."""

    @abstractmethod
    def draw(self, win):
        """Draw the piece on the board."""
        pass

    @abstractmethod
    def calculate_position(self):
        """Calculate the screen position of the piece."""
        pass