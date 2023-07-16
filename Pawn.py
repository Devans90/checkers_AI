# /* Pawn.py
import pygame
from Piece import Piece

class Pawn(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, board)
        img_path = f'images/{color}-pawn.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height))
        self.notation = 'p'