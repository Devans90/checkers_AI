# Import necessary modules
from Game import Game
from Bot import RandomBot  # Assuming you have these bot classes
from play_multiple_games import play_multiple_games
from Board import Board

import pygame

class Checkers:
	def __init__(self, screen):
		self.screen = screen
		self.running = True
		self.FPS = pygame.time.Clock()

	def _draw(self, board):
		board.draw(self.screen)
		pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Checkers")
checkers = Checkers(screen)

board_size = 8
tile_width, tile_height = 640 // board_size, 640 // board_size
board = Board(tile_width, tile_height, board_size)
checkers._draw(board)

# Create instances of your bots
# Remember to pass the appropriate color for each bot ('red' or 'black')
bot1 = RandomBot('red')
bot2 = RandomBot('black')

# Decide how many games to play
num_games = 2
game = Game(bot1, bot2)


# Play the games and get the results
bot1_wins, bot2_wins = play_multiple_games(bot1, bot2, num_games, draw=True, board=screen)

# Print the results
print(f"After {num_games} games, {bot1.__class__.__name__} won {bot1_wins} times and {bot2.__class__.__name__} won {bot2_wins} times.")