from Game import Game

def play_multiple_games(bot1, bot2, num_games):
    # Initialize win counters
    bot1_wins = 0
    bot2_wins = 0

    for i in range(num_games):
        # Create a new game
        game = Game(bot1, bot2)
        # Play the game to completion
        game.play_game()
        # Check who won and increment the appropriate counter
        if game.winner == bot1.color:
            bot1_wins += 1
        elif game.winner == bot2.color:
            bot2_wins += 1

    # Return the win-loss record for each bot
    return bot1_wins, bot2_wins