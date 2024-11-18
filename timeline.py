from gameMenu import showGameMenu
from gameSetup import setupNewGame
from gameLoop import play
from gameResults import showWinner

def timeline():
    print("playing timeline game")
    game_settings = showGameMenu()
    number_of_players = game_settings["num_of_players"]
    game_table = setupNewGame(number_of_players)
    final_hands = play(game_settings, game_table)
    showWinner(final_hands) 

timeline()


# play timeline
    # 1. game menu
    # 1.1 select number of players
    # 1.2 [bots on/off] 
    # 1.3 [difficulty level]
    # 2. setup new game
    # 2.0 shuffle deck
    # 2.1 deal starting card to each player
    # 2.2 show instructions (tell how to play game)
    # 2.3 pick starting player
    # 3. play game (player turns)
    # 3.1 starting player turn
    # 3.2 select next player
    # 3.3 take turn
    # 3.4 check if player won/game is over, if so goto 4
    # 3.5 goto 3.2
    # 4. show who winner is