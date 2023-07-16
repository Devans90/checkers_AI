from Board import Board
from Bot import Bot
import pygame

class Game:

    def __init__(self, bot1, bot2, draw=False, board=[]):
        self.bot1 = bot1
        self.bot2 = bot2
        self.winner = None
        board_size = 8
        tile_width, tile_height = 640 // board_size, 640 // board_size
        self.board = Board(tile_width, tile_height, board_size)
        self.winner = None
        self.draw = draw
        self.drawboard = board

	# checks if both colors still has a piece
    def check_piece(self, board):
        red_piece = 0
        black_piece = 0
        for y in range(board.board_size):
            for x in range(board.board_size):
                tile = board.get_tile_from_pos((x, y))
                if tile.occupying_piece != None:
                    if tile.occupying_piece.color == "red":
                        red_piece += 1
                    else:
                        black_piece += 1
        return red_piece, black_piece

                
    def play_game(self):
            if self.draw:
                self.board.draw(self.drawboard)  # Draw the initial board state
            while not self.is_game_over(self.board):
                # Get the current player's bot
                current_bot = self.bot1 if self.board.turn == self.bot1.colour else self.bot2

                move_made = False
                while not move_made:
                    # Get the bot's selected move
                    move = current_bot.select_move(self.board)
                    # Apply the move to the board
                    move_made = self.apply_move(move)
                    if self.draw:
                        self.board.draw(self.drawboard)  # Draw the board after the move
    
    def apply_move(self, move):
        # Unpack the move
        start_pos, end_pos = move
        # Get the tiles corresponding to the start and end positions
        start_tile = self.board.get_tile_from_pos(start_pos)
        end_tile = self.board.get_tile_from_pos(end_pos)
        # Get the piece to move
        piece = start_tile.occupying_piece
        # Set the selected piece on the board
        self.board.selected_piece = piece
        # Save the current position of the piece
        old_pos = piece.pos
        # Call the _move method on the piece with the end tile as argument
        piece._move(end_tile)
        # Check if the piece has moved
        if piece.pos == old_pos:
            # If the piece hasn't moved, ask the bot for another move
            print(f"The piece hasn't moved.[{self.board.turn}'s turn] Asking the bot for another move...")
            return False
        else:
            # If the piece has moved, check if the game is over
            if self.is_game_over(self.board):
                return True
            # If the piece has moved and there are no valid jumps, change the turn
            print('turn_complete')
            if not len(piece.valid_jumps()):
                self.board.turn = 'red' if self.board.turn == 'black' else 'black'
            return True

    def is_game_over(self, board):
        red_piece, black_piece = self.check_piece(board)
        if red_piece == 0 or black_piece == 0:
            self.winner = "red" if red_piece > black_piece else "black"
            return True
        else:
            return False

    def check_jump(self, board):
        piece = None
        for tile in board.tile_list:
            if tile.occupying_piece != None:
                piece = tile.occupying_piece
                if len(piece.valid_jumps()) != 0 and board.turn == piece.color:
                    board.is_jump = True
                    break
                else:
                    board.is_jump = False
        if board.is_jump:
            board.selected_piece = piece
            board.handle_click(piece.pos)
        return board.is_jump

    def message(self):
        print(f"{self.winner} Wins!!")