def showGameMenu():
    print("WELCOME to timeline")
    # number_players = input("please select number of players: ")
    number_players = 4
    bots_on = False
    bot_difficulty = 10
    return {
        "num_of_players": number_players,
        "bots_on": bots_on,
        "bot_difficulty": bot_difficulty
    }