class Card:
    """
    Card Base Type with comparison features
    """

    def __init__(self,
            symbol: str,
            symbol_rank: int,
            value: int,
            _format: str = "{v}{s}",
            special_value_format: str = None
    ):
        """
        Card Base Type with comparison features

        :param symbol: card symbol (like: spades, diamond, etc.)
        :param symbol_rank: symbol rank is required for comparing 2 cards
        :param value: card value
        :param _format: print format; {v} = value, {s} = symbol
        :param special_value_format: if set will be printed instead of value
        """

        self.symbol = symbol
        self.symbol_rank = symbol_rank
        self.value = value
        self._format = _format
        self.special_value_format = special_value_format

    def __add__(self, other) -> int:
        if isinstance(other, int):
            return self.value*self.symbol_rank + other

        if not hasattr(other, "symbol"):
            raise TypeError(f"Cannot add type '{type(self)}' and '{type(other)}'")

        return self.value + other.value

    def __radd__(self, other):
        if isinstance(other, int):
            return self.value + other

        if not hasattr(other, "symbol"):
            raise TypeError(f"Cannot add type '{type(self)}' and '{type(other)}'")

        return self.value + other.value

    def __eq__(self, other) -> bool:
        if not hasattr(other, "symbol"):
            raise TypeError(f"Cannot compare type '{type(self)}' against '{type(other)}'")

        return self.value == self.value and self.symbol_rank == other.symbol_rank

    def __gt__(self, other) -> bool:
        if not hasattr(other, "symbol"):
            raise TypeError(f"Cannot compare type '{type(self)}' against '{type(other)}'")

        if self.value == other.value:
            return self.symbol_rank > other.symbol_rank
        return self.value > other.value

    def __lt__(self, other) -> bool:
        if not hasattr(other, "symbol"):
            raise TypeError(f"Cannot compare type '{type(self)}' against '{type(other)}'")

        if self.value == other.value:
            return self.symbol_rank < other.symbol_rank
        return self.value < other.value

    def __ge__(self, other) -> bool:
        if not hasattr(other, "symbol"):
            raise TypeError(f"Cannot compare type '{type(self)}' against '{type(other)}'")

        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other) -> bool:
        if not hasattr(other, "symbol"):
            raise TypeError(f"Cannot compare type '{type(self)}' against '{type(other)}'")

        return self.__lt__(other) or self.__eq__(other)

    def __str__(self) -> str:
        return self._format.format(
            v=self.value if not self.special_value_format else self.special_value_format,
            s=self.symbol
        )

    def __repr__(self) -> str:
        return f"Card('{self.symbol}', '{self.symbol_rank}', '{self._format}')"
