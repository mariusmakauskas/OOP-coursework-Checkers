"""Main module for running the Checkers game."""

import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.game import Game

# Frames per second
FPS=60

# Initialize the game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    """Get the row and column from the mouse position."""
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    """Main function to run the Checkers game."""
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        # Check for a winner
        if game.winner() != None:
            print(game.winner())
            run = False
        
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
                
        # Update the game state
        game.update()
    
    pygame.quit()

main()