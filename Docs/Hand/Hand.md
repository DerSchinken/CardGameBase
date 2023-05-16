## Hand
These comparison operation are implemented: `<=, >=, <, >, ==`
### Functions
**.draw(amount: int, dont_take_away: bool)**  *- Draws a card from the deck.*
* `amount` - Amount of cards that will be drawn from deck (always from the top of the deck)
* `dont_take_away` (optional) - when set no card is removed from the deck and is instead put at the bottom of the deck  

**.check_rules(on_invalid: callable) -> bool or None** *- Checks if any of the rules fail.*   
* `on_invalid` (optional) - When set will be called and the return will be set as the new hand. Please see: [Hand Rules](Hand%20Rules.md)

**.get_total_value() -> int** *- Gets the total value of cards held in hand.*   

### Creating a hand
To create a new Hand you firstly need a deck for that please read these [docs](..%2FDeck%2FDeck.md).   
After doing that you can use simply use `Hand(deck)`   
#### Example:
```python
from CardGameBase.Utility import create_classic_deck
from CardGameBase import Hand
deck = create_classic_deck()

new_hand = Hand(deck)
```
> Info: While creating a hand you can set rules. Please see this: [Hand Rules](Hand%20Rules.md)
