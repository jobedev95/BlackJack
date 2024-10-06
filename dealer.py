import random
from hand import Hand
import time


class Dealer:
    """Handles the game like a real dealer in TjugoEttan. It deals out all the cards, prints both players hands, concludes the game,
    prints the results and deals the winner a point. It can also reset the game if the player wishes to play another round."""

    CARDS: list[int] = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # List of card values that can be dealt

    def __init__(self, player: Hand, computer: Hand) -> None:
        """Initialize game with one player and one computer Hand object.
        Immediately deals one card each to both."""
        self.player: Hand = player
        self.computer: Hand = computer
        self.deal_player()
        self.deal_computer()

    def deal_player(self) -> None:
        """Deal one card to player. Swap ace if possible and needed."""
        self.player.add_card(random.choice(self.CARDS))
        self.player.swap_ace()

    def deal_computer(self) -> None:
        """Deal one card to computer only if total value of current
        hand is less than 17 and the player has not already lost.
        Swap ace if possible and needed."""
        if self.player.get_value() <= 21:
            if self.computer.get_value() < 17 or self.computer.get_value() == 0:
                self.computer.add_card(random.choice(self.CARDS))
        self.computer.swap_ace()

    def print_current_hands(self) -> None:
        """Prints current hand of player and the first card of computers hand."""
        print(f"\nYour cards: {self.player.hand}, total value: {self.player.get_value()}")
        print(f"Computer's first card: {self.computer.hand[0]}")
        time.sleep(1)

    def conclude_game(self) -> None:
        """Concludes the game by dealing the final cards to computer."""
        comp_total: int = self.computer.get_value()
        while comp_total < 17:
            self.deal_computer()
            comp_total = self.computer.get_value()
        self._print_final_result()

    def _print_final_result(self) -> None:
        """Prints the final hands and the result."""
        player_value: int = self.player.get_value()
        computer_value: int = self.computer.get_value()
        print(f"\nYour final hand: {self.player.hand}, final value: {player_value}")
        print(f"Computer's final hand: {self.computer.hand}, final value: {computer_value}\n")
        time.sleep(1)

        # Checks all cases to find the winner and deals one point to the winner
        if player_value == computer_value:
            self.computer.score += 1
            print(" IT'S A DRAW - YOU LOST! ".center(60, "*"))

        elif player_value == 21:
            self.player.score += 1
            print(" YOU WON! ".center(60, "*"))

        elif computer_value == 21:
            self.computer.score += 1
            print(" YOU LOST! ".center(60, "*"))

        elif player_value > 21:
            self.computer.score += 1
            print(" YOU LOST! ".center(60, "*"))

        elif computer_value > 21:
            self.player.score += 1
            print(" YOU WON! ".center(60, "*"))

        elif player_value > computer_value:
            self.player.score += 1
            print(" YOU WON! ".center(60, "*"))

        elif computer_value > player_value:
            self.computer.score += 1
            print(" YOU LOST! ".center(60, "*"))

        self._print_score()
        time.sleep(1)

    def _print_score(self) -> None:
        """Prints current score."""
        print(f"Your score: {self.player.score}")
        print(f"Computer score: {self.computer.score}")

    def reset_game(self) -> None:
        """Empties the hands of both the player and computer."""
        self.player.empty_hand()
        self.computer.empty_hand()
