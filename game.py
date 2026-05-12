
import tkinter as tk
from deck import Deck
from hand import Hand
import random

#this basically does the games window setting size and name and color 
class BlackjackGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Double or nothing")
        self.root.geometry("700x500")
        self.root.config(bg="darkgreen")

        self.player_chips = 100
        self.win_streak = 0
       #so this is basically just some dealer quotes that will randomly show 
        self.dealer_quotes = [
            "Feeling lucky?",
            "The house always wins.",
            "Let's see what you've got.",
            "Interesting move..."
        ]

        self.create_widgets()
        self.start_new_round()

    #              WIDGETS section
    def create_widgets(self):

        self.title_label = tk.Label(
            self.root,
            text="BLACKJACK - Double or Nothing",
            font=("Arial", 24, "bold"),
            bg="darkgreen",
            fg="gold"
        )
        self.title_label.pack(pady=10)

        self.chips_label = tk.Label(
            self.root,
            text="Chips: 100",
            font=("Arial", 14),
            bg="darkgreen",
            fg="white"
        )
        self.chips_label.pack()

        self.streak_label = tk.Label(
            self.root,
            text="Win Streak: 0",
            font=("Arial", 14),
            bg="darkgreen",
            fg="white"
        )
        self.streak_label.pack()
        #quote lable that reads the random quote from the dealer

        self.quote_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12, "italic"),
            bg="darkgreen",
            fg="lightblue"
        )
        self.quote_label.pack(pady=5)

        # Dealer Section
        self.dealer_label = tk.Label(
            self.root,
            text="Dealer",
            font=("Arial", 18),
            bg="darkgreen",
            fg="white"
        )
        self.dealer_label.pack(pady=(20, 5))

        self.dealer_cards = tk.Label(
            self.root,
            text="",
            font=("Arial", 16),
            bg="darkgreen",
            fg="white"
        )
        self.dealer_cards.pack()

        # Player Section this shows the font for the player name but yeah its just a lable
        self.player_label = tk.Label(
            self.root,
            text="Player",
            font=("Arial", 18),
            bg="darkgreen",
            fg="white"
        )
        self.player_label.pack(pady=(20, 5))

        self.player_cards = tk.Label(
            self.root,
            text="",
            font=("Arial", 16),
            bg="darkgreen",
            fg="white"
        )
        self.player_cards.pack()

        # Status
        self.status_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 16, "bold"),
            bg="darkgreen",
            fg="yellow"
        )
        self.status_label.pack(pady=20)

        # Buttons
        #this section basically creates buttons for the functions of blackjack like hit and stand and new round
        button_frame = tk.Frame(self.root, bg="darkgreen")
        button_frame.pack()

        self.hit_button = tk.Button(
            button_frame,
            text="Hit",
            width=12,
            command=self.hit
        )
        self.hit_button.grid(row=0, column=0, padx=10)

        self.stand_button = tk.Button(
            button_frame,
            text="Stand",
            width=12,
            command=self.stand
        )
        self.stand_button.grid(row=0, column=1, padx=10)

        self.restart_button = tk.Button(
            button_frame,
            text="New Round",
            width=12,
            command=self.start_new_round
        )
        self.restart_button.grid(row=0, column=2, padx=10)

    # NEW ROUND 
    def start_new_round(self):

        self.deck = Deck()

        self.player_hand = Hand()
        self.dealer_hand = Hand()

        self.status_label.config(text="")

        self.hit_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)

        for _ in range(2):
            self.player_hand.add_card(self.deck.draw_card())
            self.dealer_hand.add_card(self.deck.draw_card())

        self.quote_label.config(
            text=random.choice(self.dealer_quotes)
        )

        self.update_display()

        # Blackjack check
        if self.player_hand.get_value() == 21:
            self.status_label.config(
                text="BLACKJACK! You Win!",
                fg="lime"
            )

            self.player_chips += 25
            self.win_streak += 1
            self.end_round()

    #         UPDATE DISPLAY basically is in the name and updates the display for whatever needs to be updated like text
    def update_display(self, reveal_dealer=False):

        if reveal_dealer:
            dealer_text = (
                f"{self.dealer_hand.display()} "
                f"(Value: {self.dealer_hand.get_value()})"
            )
        else:
            dealer_text = self.dealer_hand.display(hide_first=True)

        self.dealer_cards.config(text=dealer_text)

        self.player_cards.config(
            text=(
                f"{self.player_hand.display()} "
                f"(Value: {self.player_hand.get_value()})"
            )
        )

        self.chips_label.config(
            text=f"Chips: {self.player_chips}"
        )

        self.streak_label.config(
            text=f"Win Streak: {self.win_streak}"
        )

    #            basically this is for the hit function/button
    def hit(self):

        self.player_hand.add_card(
            self.deck.draw_card()
        )

        self.update_display()

        if self.player_hand.get_value() > 21:
            self.status_label.config(
                text="BUSTED! Dealer Wins!",
                fg="red"
            )

            self.player_chips -= 10
            self.win_streak = 0
            self.end_round()

    #          STAND: basicallty this allows you to stand on a certain number and the dealer to play their hand.
    def stand(self):

        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(
                self.deck.draw_card()
            )

        self.update_display(reveal_dealer=True)

        player_total = self.player_hand.get_value()
        dealer_total = self.dealer_hand.get_value()

        if dealer_total > 21:
            result = "Dealer Busts! You Win!"
            color = "lime"
            self.player_chips += 15
            self.win_streak += 1

        elif dealer_total > player_total:
            result = "Dealer Wins!"
            color = "red"
            self.player_chips -= 10
            self.win_streak = 0

        elif dealer_total < player_total:
            result = "You Win!"
            color = "lime"
            self.player_chips += 15
            self.win_streak += 1

        else:
            result = "Tie Game!"
            color = "white"

        self.status_label.config(
            text=result,
            fg=color
        )

        self.end_round()

    # END ROUND button
    def end_round(self):

        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)