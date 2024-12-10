from game_loop import show_player_cards, is_valid_placment

# print("testing show_player_cards")


test_hand = [
    {
    "title": "Amazon Echo released",
    "year": 2014,
    "month": 10,
    "description": "Amazon introduced the Echo smart speaker, which popularized voice-activated digital assistants in homes."
  },
  {
    "title": "AWS launched",
    "year": 2006,
    "month": 2,
    "description": "AWS launched its first service, Amazon S3 (Simple Storage Service), in the United States"
  },
  {
    "title": "iPhone Anncounced",
    "year": 2007,
    "month": 0,
    "description": "The first-generation iPhone was announced by then–Apple CEO Steve Jobs at Macworld, and launched later that year."
  }
]

show_player_cards(test_hand)