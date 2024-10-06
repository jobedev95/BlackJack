class Hand:
    """Acts as a real players hand in TjugoEttan. It keeps track of the current total of value of the players hand, and keeps a count on the total winning score.
    It allows for swapping the value of an ace in hand when needed. It can also empty the hand when the dealer resets the game."""

    def __init__(self) -> None:
        self.hand: list[int] = []  # Holds all the cards
        self.score: int = 0  # Keeps track of score

    def get_value(self) -> int:
        """Returns the total value of all cards currently in the hand."""
        return sum(self.hand)

    def add_card(self, card: int) -> None:
        """Adds the given card to the current hand."""
        self.hand.append(card)

    def swap_ace(self) -> None:
        """Swaps the card number 14 with 1 in case the total value of the current hand is above 21 and if there is a 14 to swap."""
        if self.get_value() > 21 and 14 in self.hand:
            self.hand[self.hand.index(14)] = 1  # Finds the index of number 14 in hand and swaps the value of that index with 1
            print("Swapped 14 with 1!")

    def empty_hand(self) -> None:
        """Empties the hand."""
        self.hand = []
