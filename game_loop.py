import random
import os

# def play(game_settings, starting_game_table ):
#     print("having lots of fun playing timeline")
#     random_player = random.randint(0, game_settings["num_of_players"]-1)
#     # current_player = 1
#     # while not game_over():
#     #     take_turn(current_player)
#     #     current_player = pick_next_player()
#     player_hands = starting_game_table["player_hands"]
#     deck = starting_game_table["deck"]
#     for i in range(9):
#         card = deck.pop()
#         player_hands[random_player].append(card)
#     return player_hands





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
        # print(f"-) {card['description']} {card['year']}")
        print(f"{card['year']} - {card['title']} ")
        print(f"{i+1})")

# Is_valid_placment: function, given a hand, new_card, and and a position; return True or False if is correct placement
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
        if new_year > hand[placment-1] and new_year < hand[placment]:
            return True
        else:
            return False

def next_player(current_player, number_of_players):
    if current_player == number_of_players - 1:
        return 0
    else:
        return current_player + 1



def play(game_settings, starting_game_table ):
    number_of_players = game_settings["num_of_players"]
    player_hands = starting_game_table["player_hands"]
    deck = starting_game_table["deck"]
    player_turn = starting_game_table["player_turn"]
    # while game not over take a a turn
     # each turn:
       # next player draws a card
       # one by one let each player take a guess until guesses
         # read card to next poerson
         # takes a guess
         # if correct guess , put into their hand
         # if wrong go to next person
    while not is_game_over(player_hands):
        drawn_card = deck.pop()
        # read card to each other player until guessed
        for i in range(number_of_players - 1):
            player_reading_to = (player_turn + 1 + i) % number_of_players
            show_player_cards(player_hands[player_reading_to])
            print("NEW CARD: ", drawn_card['description'])
            guess = int(input("where do you think that card goes? "))
            if is_valid_placment(player_hands[player_reading_to],drawn_card,guess):
                player_hands[player_reading_to].append(drawn_card)
                print("Good job thats right!")
                break
            else:
                print("SORRY you guessed wrong")
        # next players turn
        player_turn = player_turn + 1 % number_of_players

    return player_hands

def show_score(player_hands):
    # show current game score/players
    for i, p in enumerate(player_hands):
        print(f"player {i} has: {len(p)} cards")

import os
def play_fancy(game_settings, starting_game_table ):
    number_of_players = game_settings["num_of_players"]
    player_hands = starting_game_table["player_hands"]
    deck = starting_game_table["deck"]
    player_turn = starting_game_table["player_turn"]
    while not is_game_over(player_hands):
        show_score(player_hands)
        input("click when ready to play next card...")
        os.system('clear')
        drawn_card = deck.pop()
        # read card to each other player until guessed
        for i in range(number_of_players - 1):
            player_reading_to = (player_turn + 1 + i) % number_of_players
            print("-"*12)
            print(f"Player {player_reading_to} turn")
            print("-"*12)
            show_player_cards(player_hands[player_reading_to])
            print("")
            print("NEW CARD: ", drawn_card['description'])
            print("")
            guess = int(input("where do you think that card goes? "))
            if is_valid_placment(player_hands[player_reading_to],drawn_card,guess):
                player_hands[player_reading_to].append(drawn_card)
                print("Good job thats right!")
                print(f"{drawn_card['title']} in {drawn_card['year']}")
                break
            else:
                print("SORRY you guessed wrong")
                input("click when next player is ready...")
                os.system('clear')
        # next players turn
        print("")
        player_turn = player_turn + 1 % number_of_players

    return player_hands               




    return player_hands