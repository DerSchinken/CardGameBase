# Card Game Base
Create Card Games with ease
# How  to install:
`pip install CardGameBase`
or
`pip3 install CardGameBase`
# How to use:
```python
from CardGameBase.Utility import create_classic_deck
from CardGameBase import Hand

# Create a classic 52 card deck and shuffle
my_deck = create_classic_deck()
my_deck.shuffle()

# Create hands for 2 players
my_hand = Hand(my_deck)
my_friends_hand = Hand(my_deck)

# Take cards
for i in range(7):
    my_hand.draw()
    my_friends_hand.draw()

# Display both players hands
print(my_hand, f"= {my_hand.get_total_value()}")
print(my_friends_hand, f"= {my_friends_hand.get_total_value()}")

# Check who has the highest hand value
if my_hand > my_friends_hand:
    print("You won!")
else: 
    print("Your friend won!")
```

> For more Information please have look at the [Documentation](Docs%2FREADME.md).    
