# hand.py

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        total = 0
        aces = 0

        for card in self.cards:
            total += card.value()

            if card.rank == "A":
                aces += 1

        # Adjust Ace value if over 21
        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total

    def display(self, hide_first=False):
        if hide_first:
            return "?? " + " ".join(str(card) for card in self.cards[1:])
        return " ".join(str(card) for card in self.cards)