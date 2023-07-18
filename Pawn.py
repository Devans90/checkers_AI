import pygame
from Piece import Piece

class Pawn(Piece):
	def __init__(self, x, y, color, board):
		super().__init__(x, y, color, board)
		img_path = f'images/{color}-pawn.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height))
		self.notation = 'p'

	def _possible_moves(self):
		# (x, y) move for left and right
		if self.color == "red":
			possible_moves = ((-1, -1), (+1, -1)) 
		else:
			possible_moves = ((-1, +1), (+1, +1))
		return possible_moves

	def valid_moves(self):
		tile_moves = []
		moves = self._possible_moves()
		for move in moves:
			tile_pos = (self.x + move[0], self.y + move[-1])
			if tile_pos[0] < 0 or tile_pos[0] > 7 or tile_pos[-1] < 0 or tile_pos[-1] > 7:
				pass
			else:
				tile = self.board.get_tile_from_pos(tile_pos)
				if tile.occupying_piece == None:
					tile_moves.append(tile)
		return tile_moves

	def valid_jumps(self, start_pos=None):
		if start_pos is None:
			start_pos = (self.x, self.y)

		tile_jumps = []
		moves = self._possible_moves()
		for move in moves:
			tile_pos = (start_pos[0] + move[0], start_pos[1] + move[-1])
			if 0 <= tile_pos[0] <= 7 and 0 <= tile_pos[-1] <= 7:
				tile = self.board.get_tile_from_pos(tile_pos)
				if self.board.turn == self.color:
					if tile.occupying_piece != None and tile.occupying_piece.color != self.color:
						next_pos = (tile_pos[0] + move[0], tile_pos[-1] + move[1])
						if 0 <= next_pos[0] <= 7 and 0 <= next_pos[-1] <= 7:
							next_tile = self.board.get_tile_from_pos(next_pos)
							if next_tile.occupying_piece == None:
								# Add the jump to the list of valid jumps
								tile_jumps.append((next_tile, tile))  # Note the change here
								# Check if another jump is possible from the new position
								additional_jumps = self.valid_jumps(next_pos)
								tile_jumps.extend(additional_jumps)

		return tile_jumps
