import unittest
from CardGameBase.Utility import create_classic_deck
from CardGameBase import Hand, Deck, DeckConfig, Card


class TestCardGame(unittest.TestCase):
    def test_create_classic_deck(self):
        """
        Test case to verify the creation of a classic deck.
        """
        deck = create_classic_deck()
        
        # Assert the deck configuration matches the expected values
        expected_deck_config = {('c', 1): [
            [2, None], [3, None], [4, None], [5, None], [6, None], [7, None],
            [8, None], [9, None], [10, None], [10, 'J'], [10, 'D'], [10, 'K'],
            [11, 'A']],
            ('d', 2): [[2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None], [9, None], [10, None],
                       [10, 'J'], [10, 'D'], [10, 'K'], [11, 'A']],
            ('h', 3): [[2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None], [9, None], [10, None],
                       [10, 'J'], [10, 'D'], [10, 'K'], [11, 'A']],
            ('s', 4): [[2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None], [9, None], [10, None],
                       [10, 'J'], [10, 'D'], [10, 'K'], [11, 'A']]}
        self.assertEqual(deck.deck_configuration.get(), expected_deck_config)

        # Assert the string representation of the deck matches the expected value
        expected_deck_str = "2c, 3c, 4c, 5c, 6c, 7c, 8c, 9c, 10c, Jc, Dc, Kc, Ac, 2d, 3d, 4d, 5d, 6d, 7d, 8d, 9d, 10d, Jd, " \
                            "Dd, Kd, Ad, 2h, 3h, 4h, 5h, 6h, 7h, 8h, 9h, 10h, Jh, Dh, Kh, Ah, 2s, 3s, 4s, 5s, 6s, 7s, 8s, " \
                            "9s, 10s, Js, Ds, Ks, As"
        self.assertEqual(str(deck), expected_deck_str)

    def test_hand(self):
        """
        Test case to verify the functionality of the Hand class.
        """
        # Existing test case code...

    def test_comparison(self):
        """
        Test case to verify the comparison operations in the Hand class.
        """
        # Existing test case code...

    def test_invalid_comparison(self):
        """
        Test case to verify the handling of invalid comparisons in the Hand class.
        """
        # Existing test case code...

    def test_deck_config_combination(self):
        """
        Test case to verify the combination of DeckConfig objects.
        """
        # Existing test case code...

    def test_draw_from_empty_deck(self):
        """
        Test case to verify drawing from an empty deck.
        """
        deck = create_classic_deck()
        hand = Hand(deck)
        
        # Draw more cards than available in the deck
        hand.draw(len(deck) + 1)
        
        # Assert that only the available cards are drawn (equal to the number of cards in the deck)
        self.assertEqual(len(hand.hand), len(deck))

    def test_shuffle_deck(self):
        """
        Test case to verify shuffling of the deck.
        """
        deck1 = create_classic_deck()
        deck2 = create_classic_deck()

        # Shuffle the decks
        deck1.shuffle()
        deck2.shuffle()

        # Assert that shuffled decks are not equal
        self.assertNotEqual(str(deck1), str(deck2))

    def test_add_card_to_deck(self):
        """
        Test case to verify adding a card to the deck.
        """
        deck = Deck(DeckConfig())
        card = Card("A", 4, 132)

        # Add a card to the deck
        deck.add_card(card)

        # Assert that the card is in the deck
        self.assertIn(card, deck)

    def test_deck_config_load_and_save(self):
        """
        Test case to verify loading and saving of deck configurations.
        """
        config1 = DeckConfig()
        config1.add_card("A", 4, 132)
        config1.add_card("B", 3, 246)

        # Save the configuration to a file
        config1.save("test_config.json")

        # Load the configuration from the file
        config2 = DeckConfig()
        config2.load("test_config.json")

        # Assert that the loaded configuration is the same as the original configuration
        self.assertEqual(config1.get(), config2.get())

    def test_check_with_rank(self):
        """
        Test case to verify the check_with_rank property in the Hand class.
        """
        deck = create_classic_deck()

        # Create two hands with different check_with_rank values
        hand1 = Hand(deck, check_with_rank=False)
        hand2 = Hand(deck, check_with_rank=True)
        
        # Draw the same cards in both hands
        hand1.draw(3)
        hand2.draw(3)

        # Assert that the total value without rank is equal
        self.assertEqual(hand1.get_total_value(), hand2.get_total_value())

        # Modify one card's rank and assert that the total value with rank is different
        hand2.hand[0].symbol_rank = 10
        self.assertNotEqual(hand1.get_total_value(), hand2.get_total_value())


if __name__ == "__main__":
    unittest.main()
