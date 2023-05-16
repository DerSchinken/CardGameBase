## Card
**Card(symbol: str, symbol_rank: int, value: int, _format: str, special_value_format: str)** *- Generates a deck from the DeckConfig*    
* `symbol` - Symbol of the cards (like c for clubs or s for spades and so on)
* `symbol_rank` - Symbol rank (for example clubs is the lowest so 1, and spades the highest so 4) 
* `value` - Value of the card
* `_format` (Optional) - format for how the card should get displayed (`{v}` - value, `{s}` - symbol)
* `special_value_format` (Optional) - Used instead for `{v}` when set

These comparison operation(s) are implemented: `==, >=, <=, >, <, +`   
### Functions

**.shuffle() -> None** *- Shuffles the deck.*     

**.add_card(cards: Card | list[Card] | DeckConfig) -> None** *- Adds a card to the bottom of the deck*
* `cards` - Card, a list of Cards or DeckConfig of which all cards will be added

**.get_card(amount: int, put_to_bottom: bool) -> Card | list[Card]**      
* `amount` - Amount of cards that will be drawn
* `put_to_bottom` (default False) - Also put the cards to the bottom

**.reload() -> None** *- Resets the deck to the deck config*

**.get_all_symbols() -> set[str]** *- Returns all symbols that exist in that deck*
