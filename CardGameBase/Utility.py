from . import DeckConfig, Deck


def create_classic_deck() -> Deck:
    """
    Creates a classic deck with 52 cards of clubs, spades, diamonds and hearts (2 - Ace)

    :return: The Deck
    """
    symbols = [('c', 1), ('d', 2), ('h', 3), ('s', 4)]
    deck_config = DeckConfig()

    for symbol, symbol_rank in symbols:
        for card_value in range(2, 14 + 1):
            # 10 = 10, 11 = j, 12 = d, 13 = j, 14 = k
            if card_value == 11:
                deck_config.add_card(symbol, symbol_rank, 10, "J")
            elif card_value == 12:
                deck_config.add_card(symbol, symbol_rank, 10, "D")
            elif card_value == 13:
                deck_config.add_card(symbol, symbol_rank, 10, "K")
            elif card_value == 14:
                deck_config.add_card(symbol, symbol_rank, 11, "A")
            else:
                deck_config.add_card(symbol, symbol_rank, card_value)

    return Deck(deck_config)
