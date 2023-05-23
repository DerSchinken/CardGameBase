from __future__ import annotations

from typing import Iterable, List, Set
from . import Card, EmptyDeck
from random import shuffle
import pickle


class DeckConfig:
    """
    Deck config structure:
        __deck = {
            (symbol, symbol_rank): [
                [value, special_value_format1],
                ...
            ],
            ...
        }
    """
    __deck_config: dict[tuple: List[List[int, str]]]

    def __init__(self, deck_config: dict[tuple: List[List[int, str]]] = None):
        if deck_config is None:
            deck_config = {}
        self.__deck_config: dict[tuple: List[List[int, str]]] = deck_config

    def add_card(self, symbol: str, symbol_rank: int, value: int, special_value_format: str = None) -> None:
        """
        Adds a card to the deck config

        :param symbol: Card symbol
        :param symbol_rank: symbol rank (for comparison when cards have the same value)
        :param value: card value
        :param special_value_format: is displayed instead of the card value when set
        :return:
        """
        key = (symbol, symbol_rank)
        if not self.__deck_config.get(key):
            self.__deck_config[key] = [[value, special_value_format]]
        else:
            # if [value, special_value_format] in self.__deck[key]:
            #    raise KeyError(f"a card with '{symbol=}', '{symbol_rank=}', '{value=}'; already exists!")
            self.__deck_config[key].append([value, special_value_format])

    def get(self) -> dict[tuple: List[List[int, str]]]:
        """
        :return: gives back a deck config copy
        """
        return self.__deck_config.copy()

    def load(self, file: str) -> None:
        """
        Load deck config from file
        """
        with open(file, "rb") as f:
            self.__deck_config = pickle.load(f)

    def save(self, file: str) -> None:
        """
        save deck config to file
        """
        with open(file, "wb") as f:
            pickle.dump(self.__deck_config, f)

    def __add__(self, other):
        if not type(self) == type(other):  # hasattr(other, "_DeckConfig__deck_config"):
            raise TypeError(f"Cannot add type '{type(self)}' and '{type(other)}'")

        new_deck = self.__deck_config.copy()
        for symbol, symbol_rank in other.get().keys():
            if new_deck.get((symbol, symbol_rank)):
                new_deck[(symbol, symbol_rank)].append(other.get()[(symbol, symbol_rank)])
            else:
                new_deck[(symbol, symbol_rank)] = other.get()[(symbol, symbol_rank)]
        return new_deck


class Deck:
    def __init__(self, deck_configuration: DeckConfig = None):
        """
        :param deck_configuration: Deck Configuration
        """
        if deck_configuration is None:
            deck_configuration = DeckConfig()
        self.deck_configuration = deck_configuration
        self.cards: List[Card] = []
        self.__iterator = 0

        self.__create(self.deck_configuration)

    def __create(self, deck_config: DeckConfig) -> None:
        """
        Creates cards with the deck configuration
        """
        deck = deck_config.get()
        for card_symbol, card_symbol_rank in deck:
            # print(deck[(card_symbol, card_symbol_rank)])
            for card_value, special_value_format in deck[(card_symbol, card_symbol_rank)]:
                self.cards.append(Card(
                    card_symbol,
                    card_symbol_rank,
                    card_value,
                    special_value_format=special_value_format
                ))

    def shuffle(self) -> None:
        """
        Shuffle the deck
        """
        cards_before = self.cards.copy()
        # Since random can also create the same deck as before
        # would be extremely rare, but it could happen.
        # And if the deck is smaller than or equal to 1 this would
        # create a infinite loop
        while self.cards == cards_before and len(self.cards) > 1:
            shuffle(self.cards)

    def get_card(self, amount: int = 1, put_to_bottom: bool = False) -> Card | List[Card]:
        """
        Returns the top card of the deck and removes the card from the deck

        :param amount: Amount of cards to draw
        :param put_to_bottom: Don't remove card when taking one from top and put it at the bottom
        :return: {amount} amount of cards
        """
        if not len(self.cards) >= amount and not put_to_bottom:
            raise EmptyDeck("Deck has not enough cards or is empty.")

        cards = []
        for i in range(amount):
            cards.append(self.cards.pop(0))
            if put_to_bottom:
                self.cards.append(cards[-1])

        return cards[0] if len(cards) == 1 else cards

    def add_card(self, cards: Card | List[Card] | DeckConfig) -> None:
        """
        Adds card(s) to bottom of the deck

        :param cards: The card(s) to add
        """
        if isinstance(cards, list):
            self.cards.extend(cards)
        elif isinstance(cards, DeckConfig):
            self.__create(cards)
        else:
            self.cards.append(cards)

    def reload(self) -> None:
        """
        Resets the Deck to the deck_configuration
        """
        self.cards = []
        self.__iterator = 0
        self.__create(self.deck_configuration)

    def get_all_symbols(self) -> Set[str]:
        """
        Returns a set of card symbols
        :return: a set of all card symbols
        """
        symbols = set()
        for card in self.cards:
            symbols.add(card.symbol)
        # return {card.symbol for card in self.cards}
        return symbols

    def __contains__(self, card: Card) -> bool:
        return card in self.cards

    def __iter__(self) -> Iterable[Card]:
        return self.cards.__iter__()

    def __next__(self) -> Card:
        self.__iterator += 1
        if self.__iterator > len(self.cards):
            return self.cards[self.__iterator]
        raise StopIteration

    def __str__(self) -> str:
        return ', '.join(map(lambda _: str(_), self.cards))
