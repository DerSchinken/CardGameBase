from CardGameBase.Utility import create_classic_deck
from CardGameBase import Hand


def check_player_hand(hand, rule):
    print("You have too much. You lose!\n")
    init()


def check_dealer_hand(hand, rule):
    print("Dealer has too much. You Win!\n")
    init()


def init():
    deck.shuffle()
    player_hand.hand, dealer_hand.hand = [], []
    while player_hand.check_rules() or dealer_hand.check_rules():
        player_hand.hand, dealer_hand.hand = [], []
        for o in range(3):
            player_hand.draw(dont_take_away=True)
            dealer_hand.draw(dont_take_away=True)


deck = create_classic_deck()
player_hand = Hand(deck, rules="{total_value} > 21")
dealer_hand = Hand(deck, rules="{total_value} > 21")
init()

while True:
    print(f"Dealer Hand: {dealer_hand} = {dealer_hand.get_total_value()}")
    print(f"{player_hand} = {player_hand.get_total_value()}")
    dealer_hand.check_rules(check_dealer_hand)
    player_hand.check_rules(check_player_hand)
    choice = input("Take one more Card? [y/n]: ")
    if choice == "y":
        player_hand.draw(dont_take_away=True)
        print(f"{player_hand} = {player_hand.get_total_value()}")
    else:
        if player_hand > dealer_hand:
            print("You win!\n")
        elif player_hand == dealer_hand:
            player_hand.check_with_rank, dealer_hand.check_with_rank = True, True
            if player_hand > dealer_hand:
                print("You win!\n")
            elif player_hand < dealer_hand:
                print("You lose\n")
            else:
                print("Tie!\n")
            player_hand.check_with_rank, dealer_hand.check_with_rank = False, False
        else:
            print("You lose!\n")
        init()
    dealer_hand.draw(dont_take_away=True)
# Perfect 50 line BlackJack, could probably make it even smaller but idc lol (also perfect 50 lines :D)
