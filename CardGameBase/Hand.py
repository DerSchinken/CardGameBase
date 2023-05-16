from typing import Iterable

from . import Deck, Card

class Hand:
    def __init__(self, deck: Deck, rules: str |  bool = None, check_with_rank: bool = False):
        """
        :param deck: Deck from which cards will be drawn
        :param rules: rules for the hand; Please see the documentation for more info!
        """
        self.hand: list[Card] = []
        self.deck = deck
        self.rules = rules
        self.__iterator = 0
        self.check_with_rank = check_with_rank

    def draw(self, amount: int = 1, dont_take_away: bool = False) -> None:
        """
        Draw {amount} amount of card(s)

        :param amount: amount of cards to be drawn
        :param dont_take_away: Don't take the cards away from deck and put to the bottom of the deck
        """
        if amount > 1:
            self.hand.extend(self.deck.get_card(amount, dont_take_away))
        else:
            self.hand.append(self.deck.get_card(amount, dont_take_away))

    def empty(self, put_back: bool=True) -> None:
        """
        Removes cards from hand

        :param put_back: when true puts cards back to the deck
        """
        if put_back:
            self.deck.add_card(self.hand)
        self.hand = []

    def check_rules(self, on_invalid: callable = None) -> None | str:
        """
        Check if the hand is valid

        :param on_invalid: callback function when the hand is invalid; if none exception will be raised
        :return: if on_invalid is given none else the rule that failed will be returned
        """
        # on_invalid(invalid_hand, rule)
        # raise NotImplementedError("Coming Soon")

        if not self.hand:
            return "Empty Hand"

        special_vars = {
            "total_value": self.get_total_value(),
            "total_value_rank": self.get_total_value(with_rank=True),
            "count_cards": len(self.hand)
        }
        for symbol in self.deck.get_all_symbols():
            special_vars.update({
                f"total_value{symbol}": lambda: eval(f"self.get_total_value({symbol})"),
                f"total_value_rank{symbol}": lambda: eval(f"self.get_total_value({symbol}, True)")
            })

        if isinstance(self.rules, list):
            for rule in self.rules:
                if eval(rule.format(**special_vars)):
                    if not on_invalid:
                        return rule

                    fixed_hand = on_invalid(self.hand, rule)
                    if not fixed_hand is None:
                        self.hand = fixed_hand
                    return rule
        else:
            if eval(self.rules.format(**special_vars)):
                if not on_invalid:
                    return self.rules

                fixed_hand = on_invalid(self.hand, self.rules)
                if not fixed_hand is None:
                    self.hand = fixed_hand
                return self.rules

    def get_total_value(self, symbol : str = None, with_rank: bool = False) -> int:
        _sum = 0
        if symbol:
            if with_rank:
                for card in self.hand:
                    if card.symbol == symbol:
                        _sum += card.value * card.symbol_rank
                return _sum

            for card in self.hand:
                if card.symbol == symbol:
                    _sum += card.value
            return _sum

        if with_rank:
            for card in self.hand:
                _sum += card.value * card.symbol_rank
            return _sum
        return sum(self.hand)

    @property
    def check_with_rank(self) -> bool:
        return self.__check_with_rank

    @check_with_rank.setter
    def check_with_rank(self, value: bool) -> None:
        self.__check_with_rank = value

    def __eq__(self, other) -> bool:
        if not hasattr(other, "hand"):
            raise TypeError(f"Cannot compare type '{type(self)}' against '{type(other)}'")

        self_total_value, other_total_value = 0, 0
        if self.check_with_rank:
            for card in self.hand:
                self_total_value += card.value * card.symbol_rank
            for card in other.hand:
                other_total_value += card.value * card.symbol_rank
        else:
            self_total_value = sum(self.hand)
            other_total_value += sum(other.hand)

        return self_total_value == other_total_value

    def __gt__(self, other) -> bool:
        if not hasattr(other, "hand"):
            raise TypeError(f"Cannot compare type '{type(self)}' against '{type(other)}'")

        self_total_value, other_total_value = 0, 0
        if self.check_with_rank:
            for card in self.hand:
                self_total_value += card.value * card.symbol_rank
            for card in other.hand:
                other_total_value += card.value * card.symbol_rank
        else:
            self_total_value = sum(self.hand)
            other_total_value += sum(other.hand)

        return self_total_value > other_total_value

    def __lt__(self, other) -> bool:
        if not hasattr(other, "hand"):
            raise TypeError(f"Cannot compare type '{type(self)}' against '{type(other)}'")

        self_total_value, other_total_value = 0, 0
        if self.check_with_rank:
            for card in self.hand:
                self_total_value += card.value * card.symbol_rank
            for card in other.hand:
                other_total_value += card.value * card.symbol_rank
        else:
            self_total_value = sum(self.hand)
            other_total_value += sum(other.hand)

        return self_total_value < other_total_value

    def __ge__(self, other) -> bool:
        if not hasattr(other, "hand"):
            raise TypeError(f"Cannot compare type '{type(self)}' against '{type(other)}'")

        self_total_value, other_total_value = 0, 0
        if self.check_with_rank:
            for card in self.hand:
                self_total_value += card.value * card.symbol_rank
            for card in other.hand:
                other_total_value += card.value * card.symbol_rank
        else:
            self_total_value = sum(self.hand)
            other_total_value += sum(other.hand)

        return self_total_value >= other_total_value

    def __le__(self, other) -> bool:
        if not hasattr(other, "hand"):
            raise TypeError(f"Cannot compare type '{type(self)}' against '{type(other)}'")

        self_total_value, other_total_value = 0, 0
        if self.check_with_rank:
            for card in self.hand:
                self_total_value += card.value * card.symbol_rank
            for card in other.hand:
                other_total_value += card.value * card.symbol_rank
        else:
            self_total_value = sum(self.hand)
            other_total_value += sum(other.hand)

        return self_total_value <= other_total_value

    def __contains__(self, card: Card) -> bool:
        return card in self.hand

    def __iter__(self) -> Iterable[Card]:
        return self.hand.__iter__()

    def __next__(self) -> Card:
        self.__iterator += 1
        if self.__iterator > len(self.hand):
            return self.hand[self.__iterator]
        raise StopIteration

    def __str__(self):
        return ', '.join(map(lambda _: str(_), self.hand))
