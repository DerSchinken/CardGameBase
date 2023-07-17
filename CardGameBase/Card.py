class Card:
    """
    Card Base Type with comparison features
    """

    def __init__(self,
                 symbol: str,
                 symbol_rank: int,
                 value: int,
                 card_format: str = "{v}{s}",
                 special_value_format: str = None,
                 calculate_with_rank: bool = False,
                 ):
        """
        Card Base Type with comparison features

        :param symbol: card symbol (like: spades, diamond, etc.)
        :param symbol_rank: symbol rank is required for comparing 2 cards
        :param value: card value
        :param card_format: print format; {v} = value, {s} = symbol
        :param special_value_format: if set will be printed instead of value
        """

        self.symbol = symbol
        self.symbol_rank = symbol_rank
        self.value = value
        self.card_format = card_format
        self.special_value_format = special_value_format
        self.calculate_with_rank = calculate_with_rank

    def _check_type(self, other):
        exceptions = ["int"]
        if not isinstance(other, self.__class__) and not type(other).__name__ in exceptions:
            raise NotImplementedError(f"Cannot perform operation between '{type(self).__name__}' and '{type(other).__name__}'")

    def __add__(self, other) -> int:
        self._check_type(other)

        if isinstance(other, int):
            return self.value + other
        if self.calculate_with_rank:
            return self.value * self.symbol_rank + other

        return self.value + other.value

    def __radd__(self, other):
        self._check_type(other)

        if isinstance(other, int):
            return self.value + other
        if self.calculate_with_rank:
            return self.value * self.symbol_rank + other
        return self.value + other.value

    def __eq__(self, other) -> bool:
        self._check_type(other)

        if isinstance(other, int):
            return self.value == other
        if self.calculate_with_rank:
            return self.value == other.value and self.symbol_rank == other.symbol_rank
        return self.value == other.value

    def __gt__(self, other) -> bool:
        self._check_type(other)

        if isinstance(other, int):
            return self.value > other
        if self.value == other.value and self.calculate_with_rank:
            return self.symbol_rank > other.symbol_rank
        return self.value > other.value

    def __lt__(self, other) -> bool:
        self._check_type(other)

        if isinstance(other, int):
            return self.value < other
        if self.value == other.value and self.calculate_with_rank:
            return self.symbol_rank < other.symbol_rank
        return self.value < other.value

    def __ge__(self, other) -> bool:
        self._check_type(other)

        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other) -> bool:
        self._check_type(other)

        return self.__lt__(other) or self.__eq__(other)

    def __str__(self) -> str:
        return self.card_format.format(
            v=self.value if not self.special_value_format else self.special_value_format,
            s=self.symbol
        )

    def __repr__(self) -> str:
        return f"Card('{self.symbol}', '{self.symbol_rank}', '{self.card_format}')"
