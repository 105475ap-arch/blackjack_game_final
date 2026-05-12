# test_blackjack.py

# test_blackjack.py

from card import Card
from deck import Deck
from hand import Hand


#      CARD TESTS 
def test_card_values():

    king = Card("♠", "K")
    ace = Card("♥", "A")
    five = Card("♦", "5")

    assert king.value() == 10
    assert ace.value() == 11
    assert five.value() == 5

    print("Card value tests passed!")


#    DECK TESTS 

def test_deck():

    deck = Deck()

    # Deck should start with 52 cards
    assert len(deck.cards) == 52

    # Drawing one card should reduce size
    deck.draw_card()

    assert len(deck.cards) == 51

    print("Deck tests passed!")


#       HAND TESTS -

def test_hand_values():

    hand = Hand()

    hand.add_card(Card("♠", "10"))
    hand.add_card(Card("♥", "7"))

    assert hand.get_value() == 17

    print("Hand value test passed!")


#    Ace testing

def test_ace_adjustment():

    hand = Hand()

    hand.add_card(Card("♠", "A"))
    hand.add_card(Card("♥", "K"))
    hand.add_card(Card("♦", "5"))

    # Should become 16 instead of 26
    assert hand.get_value() == 16

    print("Ace adjustment test passed!")


#    Main test.

if __name__ == "__main__":

    test_card_values()
    test_deck()
    test_hand_values()
    test_ace_adjustment()

    print("\nAll tests passed!")