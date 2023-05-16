## Set rules for a hand  
Rules when for when a hand is invalid, an example: (blackjack) {total_value} > 21.   
> [Info]: Rules will not be checked automatically to check rules please use `.check_rules()` when you want to do that.   
### How to set rules
When creating a new hand you can set rules (second argument)   
Rules will not be checked automatically to check rules please use `.check_rules()` when you want to do that.
#### Special Variables
`count_cards` - Count how many cards you have   
`total_value` - Total Value of cards in hand (without symbol rank multiplier)   
`total_value_rank` - Total Value of cards in hand (with rank multiplier)   
`total_value[symbol]` and `total_value_rank[symbol]` - Get total value from specific symbols    
#### Example:
```python
# For copy & paste quick testing please ignore
from CardGameBase.Utility import create_classic_deck
from CardGameBase import Hand
deck = create_classic_deck()

#######################
# Example begins here #
#######################
hand = Hand(deck, rules=[
    "{count_cards} > 100",
    "{total_value} > 21",
    "{total_value_rankc} == 10", # c stands for clubs and is the symbol here
])
```

### Check the rules
When checking the rules you have 2 options:
1. Just check the rules and when one fails return the rule that failed
2. Call a callback function to fix the hand or do something else

**.check_rules(on_invalid: callable) -> bool or None**
* `on_invalid` - Callback function   

#### Callback function
A callback function needs to get 2 Arguments: `invalid_hand (type: list[Card])` and `failed_rule (type: str)` (you can ofc name them whatever you want)    
and it can return a new maybe now valid hand which will be set as the new hand. If the return is None the hand will not change

#### Example:
```python
# For copy & paste quick testing please ignore
from CardGameBase.Utility import create_classic_deck
from CardGameBase import Hand, Card
deck = create_classic_deck()
hand = Hand(deck, rules=[
    "{count_cards} > 100",
    "{total_value} > 21",
    "{total_value_rankc} == 10", # c stands for clubs and is the symbol here
])

#######################
# Example begins here #
#######################
def callback_function(invalid_hand: list[Card], failed_rule: str) -> list[Card]:
    # Do something to make the hand valid again, example:
    if failed_rule == "{count_cards} > 100": # when hand has more than 100 cards set to only 60 cards
        now_valid_hand = invalid_hand[:60]
    else: # Else just reset it
        now_valid_hand = []
    return now_valid_hand

hand.check_rules(callback_function)
```
