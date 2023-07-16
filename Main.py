import pygame
from Board import Board
from Game import Game
from Bot import RandomBot

pygame.init()

class Checkers:
	def __init__(self, screen):
		self.screen = screen
		self.running = True
		self.FPS = pygame.time.Clock()

	def _draw(self, board):
		board.draw(self.screen)
		pygame.display.update()

	def main(self, window_width, window_height):
		board_size = 8
		tile_width, tile_height = window_width // board_size, window_height // board_size
		board = Board(tile_width, tile_height, board_size)
		game = Game()
		while self.running:
			game.check_jump(board)

			for self.event in pygame.event.get():
				if self.event.type == pygame.QUIT:
					self.running = False

				if not game.is_game_over(board):
					if self.event.type == pygame.MOUSEBUTTONDOWN:
						board.handle_click(self.event.pos)
				else:
					game.message()
					self.running = False

			self._draw(board)
			self.FPS.tick(60)



# if __name__ == "__main__":
# 	# window_size = (640, 640)
# 	# screen = pygame.display.set_mode(window_size)
# 	# pygame.display.set_caption("Checkers")

# 	# checkers = Checkers(screen)
# 	# checkers.main(window_size[0], window_size[1])


#     def play_multiple_games(bot1, bot2, num_games):
#         # Initialize win counters
#         bot1_wins = 0
#         bot2_wins = 0

#         for i in range(num_games):
#             # Create a new game
#             game = Game(bot1, bot2)
#             # Play the game to completion
#             game.play_game()
#             # Check who won and increment the appropriate counter
#             if game.winner == bot1.color:
#                 bot1_wins += 1
#             elif game.winner == bot2.color:
#                 bot2_wins += 1

#         # Return the win-loss record for each bot
#         return bot1_wins, bot2_wins
    
#     bot1_wins, bot2_wins = play_multiple_games(RandomBot, RandomBot, 5)