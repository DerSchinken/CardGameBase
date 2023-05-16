## DeckConfig
**DeckConfig(deck_config: dict[tuple: list[list[int, str]]])** *- Creates a deck configuration*    
* `deck_config` (Optional) - Existing deck config

These comparison operation(s) are implemented: `+`
### Functions
**.add_card(symbol: str, symbol_rank: int, value: int, special_value_format: str) -> None** *- Adds a card to the deck configuration*
* `symbol` - Symbol of the card
* `symbol_rank` - Symbol Rank
* `value` - Value of the card
* `special_value_format` (optional) - Is displayed instead of the number when set

**.get() -> dict[tuple: list[list[int, str]]]** *- Gets the deck configuration in a dict format*

**.load(file: str) -> None** *- Loads a deck configuration from a file*
* `file` - File from where the deck configuration shall be loaded

**.save(file: str)** *- Saves the deck config with pickle*
* `file` - File from where the deck configuration shall be saved
