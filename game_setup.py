import json
import random


def shuffle_cards(deck):
    random.shuffle(deck)
    return deck

def setupNewGame(number_of_players):
    # 0 load cards from json file
    deck = []
    print("loading game cards...")
    with open('cards.json') as f:
        deck = json.load(f)

    print(f"setting up game for {number_of_players} players")
    # 1 pick staring player, always player 0, maybe later randomize
    starting_player = 0
    # 2 shuffel deck
    shuffled_deck = shuffle_cards(deck)
    # 3 deal each player 1 card
    player_hands = []
    for i in range(number_of_players):
        player_hand = [shuffled_deck.pop()]
        player_hands.append(player_hand)


    return {
        "player_turn": starting_player,
        "player_hands": player_hands,
        "deck":shuffled_deck
    }