from CardGameBase.Utility import create_classic_deck
from CardGameBase import Hand
from random import randint

deck = create_classic_deck()
deck.shuffle()
bots = list(map(lambda _: _.draw(3) or _, [Hand(deck) for _ in range(3)]))

player = Hand(deck)
player.draw(3)

middle_field = Hand(deck)
middle_field.draw(3)

get_max = lambda __: max(__.get_total_value(_) for _ in ["d", "h", "s", "c"])


def print_playing_field(show_all: bool = False) -> None:
    if show_all:
        for _i, _bot in enumerate(bots):
            print(f"Bot {_i + 1}: {_bot} = {get_max(_bot)}")
    else:
        print(middle_field, f"= {get_max(middle_field)}")
    print(player, f"= {get_max(player)}")


def check_game():
    print_playing_field(True)
    win = True
    for _bot in bots:
        if not get_max(player) > get_max(_bot):
            win = False
            break

    print("You won!\n\n") if win else print("You lose!\n\n")

    deck.reload()
    deck.shuffle()
    for _bot in bots:
        _bot.empty()
        _bot.draw(3)

    player.empty()
    player.draw(3)

    middle_field.empty()
    middle_field.draw(3)


while True:
    closed = False
    print_playing_field()

    choice = input("Take card, switch all 3 cards and close or close [t, s, c]: ")
    if choice == "t":
        take_card = int(input("Which card do you want [1-3]: ")) - 1
        switch_card = int(input("Which card do you wish to switch [1-3]: ")) - 1
        x = middle_field.hand.pop(take_card)
        y = player.hand.pop(switch_card)
        player.hand.insert(switch_card, x)
        middle_field.hand.insert(take_card, y)
    elif choice == "s":
        x = player.hand.copy()
        y = middle_field.hand.copy()
        player.hand = y
        middle_field.hand = x
        closed = True
    elif choice == "c":
        closed = True
    for i, bot in enumerate(bots):
        take_card = randint(0, 2)
        switch_card = randint(0, 2)
        x = middle_field.hand.pop(take_card)
        y = bot.hand.pop(switch_card)
        bot.hand.insert(switch_card, x)
        middle_field.hand.insert(take_card, y)
        print(f"Bot {i + 1} takes {x} in exchange for {y}")
    if closed:
        check_game()
