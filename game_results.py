
def showWinner(final_hands):
    # 4.1 show how many cards each player ended with
    winning_player = 0
    winning_player_score = 0
    for i, hand in enumerate(final_hands):
        print(f" player {i} had {len(hand)} cards!")
        if len(hand) > winning_player_score:
            winning_player = i
            winning_player_score = len(hand)
    # 4.2 say who won
    print(f"player {winning_player} Won!!")
    # print(final_hands)

