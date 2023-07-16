from abc import ABC, abstractmethod
import random

def get_legal_moves(board, colour):
    """
    Given the current board state and the current player color, return a list of legal moves.
    Each move could be represented as a tuple of coordinates, for example:
    ((start_row, start_col), (end_row, end_col))
    """
    legal_moves = []
    # Iterate over all squares on the board
    for tile in board.tile_list:
        piece = tile.occupying_piece
        # If the square contains one of the current player's pieces
        if piece is not None and piece.color == colour:
            # Check all possible moves for this piece
            for move in piece.valid_moves():
                legal_moves.append((piece.pos, move.pos))
            # Check all possible jumps for this piece
            for jump in piece.valid_jumps():
                legal_moves.append((piece.pos, jump[0].pos))
    return legal_moves


class Bot(ABC):
    def __init__(self, colour) -> None:
        self.colour = colour

    @abstractmethod
    def select_move(self, game_state):
        """
        Given the current game_state, return the bot's chosen move.
        The format of game_state and the move will depend on the specifics of your game implementation.
        """
        pass

class RandomBot(Bot):
    def select_move(self, game_state):
        # This bot selects a move randomly from the list of legal moves.
        # Note: You'll need to implement the get_legal_moves function.
        legal_moves = get_legal_moves(game_state, self.colour)
        return random.choice(legal_moves)
