# Should write an actual good unit test or smth but idc enough rn so this has to do it
from CardGameBase.Utility import create_classic_deck
from CardGameBase import Hand, Deck, DeckConfig, Card

x = create_classic_deck()
print(x)

if not x.deck_configuration.get() == {('c', 1): [
    [2, None], [3, None], [4, None], [5, None], [6, None], [7, None],
    [8, None], [9, None], [10, None], [10, 'J'], [10, 'D'], [10, 'K'],
    [11, 'A']],
    ('d', 2): [[2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None], [9, None], [10, None],
               [10, 'J'], [10, 'D'], [10, 'K'], [11, 'A']],
    ('h', 3): [[2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None], [9, None], [10, None],
               [10, 'J'], [10, 'D'], [10, 'K'], [11, 'A']],
    ('s', 4): [[2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None], [9, None], [10, None],
               [10, 'J'], [10, 'D'], [10, 'K'], [11, 'A']]}:
    raise ValueError("Deck configuration is different than expected")

if not str(x) == "2c, 3c, 4c, 5c, 6c, 7c, 8c, 9c, 10c, Jc, Dc, Kc, Ac, 2d, 3d, 4d, 5d, 6d, 7d, 8d, 9d, 10d, Jd, Dd, " \
                 "Kd, Ad, 2h, 3h, 4h, 5h, 6h, 7h, 8h, 9h, 10h, Jh, Dh, Kh, Ah, 2s, 3s, 4s, 5s, 6s, 7s, 8s, 9s, 10s, " \
                 "Js, Ds, Ks, As":
    raise ValueError("Deck is different than expected")

x.shuffle()
print(x)

test_hand = Hand(x)
test_hand.draw(5213, True)
print(test_hand)
print(test_hand == test_hand)
print(test_hand >= test_hand)
print(test_hand <= test_hand)
print(test_hand > test_hand)
print(test_hand < test_hand)

y = Deck(DeckConfig())
y_hand = Hand(y)
y.add_card(Card("A", 4, 132))
y.add_card([Card("B", 2, 135)] * 1230)
y_hand.draw(200)
print(y_hand)

for card in x:
    print(card, end=" ")

print("\n", test_hand == y_hand, sep="")
print(test_hand >= y_hand)
print(test_hand <= y_hand)
print(test_hand > y_hand)
try:
    print(test_hand < y)
except TypeError:
    print(test_hand < y_hand)
else:
    raise Exception("This shouldn't work")

x = DeckConfig()
x.add_card("123", 123, 17342382)
x.add_card("123", 123, 17342382)
x.add_card("123", 123, 17342382)
x.add_card("133", 123, 17342382)
y = DeckConfig()
y.add_card("123", 123, 17342382)
print(y + x, x + y, sep="\n")
try:
    y + 1
except TypeError:
    pass
else:
    raise Exception("This shouldn't work")
