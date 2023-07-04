class EmptyDeck(Exception):
    """
    Exception raised when attempting to perform an operation on an empty deck.
    """

    def __init__(self, message="The deck is empty."):
        self.__message = message
        super().__init__(self.__message)

    def __str__(self):
        return self.__message
