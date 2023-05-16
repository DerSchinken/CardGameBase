## Deck
**Deck(deck_config: DeckConfig)** *- Generates a deck from the DeckConfig*    
* `deck_config` - Deck Config      

These comparison operation(s) are implemented: `in`   
### Functions

**.shuffle() -> None** *- Shuffles the deck.*     

**.add_card(cards: Card | list[Card] | DeckConfig) -> None** *- Adds a card to the bottom of the deck*
* `cards` - Card, a list of Cards or DeckConfig of which all cards will be added

**.get_card(amount: int, put_to_bottom: bool) -> Card | list[Card]**      
* `amount` - Amount of cards that will be drawn
* `put_to_bottom` (default False) - Also put the cards to the bottom

**.reload() -> None** *- Resets the deck to the deck config*

**.get_all_symbols() -> set[str]** *- Returns all symbols that exist in that deck*
