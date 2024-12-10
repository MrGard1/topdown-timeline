import random

def play(game_settings, starting_game_table ):
    print("having lots of fun playing timeline")
    random_player = random.randint(0, game_settings["num_of_players"]-1)
    # current_player = 1
    # while not game_over():
    #     take_turn(current_player)
    #     current_player = pick_next_player()
    player_hands = starting_game_table["player_hands"]
    deck = starting_game_table["deck"]
    for i in range(9):
        card = deck.pop()
        player_hands[random_player].append(card)
    return player_hands

# is_game_over: a function, which given your game state return a bool if game is over
def is_game_over(player_hands):
    for hand in player_hands:
        if len(hand) >= 10:
            return True
    return False

# show_player_cards: a function, given a player hand, display it in a way that a placement can be selected
def show_player_cards(hand):
    hand = sorted(hand, key=lambda card: card['year'])
    print("0)")
    for i, card in enumerate(hand):
        print(f"-) {card['description']} {card['year']}")
        print(f"{i+1})")

def is_valid_placment(hand, new_card, placment):
    hand = sorted(hand, key=lambda card: card['year'])
    new_year = new_card['year']
    if placment == 0:
        if new_year < hand[0]['year']:
            return True
        else:
            return False
    elif placment == len(hand):
        if new_year > hand[-1]['year']:
            return True
        else:
            return False
    else:
        if new_year > card[placment-1] and new_year < card[placment]:
            return True
        else:
            return False