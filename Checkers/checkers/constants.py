"""
Constants for the Checkers game.
"""

import pygame

# Window dimensions
WIDTH = 800
HEIGHT = 800
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH // COLS

# Colors
GREY_PIECES=(78,78,78)
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
BLUE=(0, 0, 255)
GREY_BORDER=(128, 128, 128)

# Crown image for kings
CROWN=pygame.transform.scale(
    pygame.image.load('checkers/assets/crown.png'), (62, 50)
)