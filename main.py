import pyinputplus as py
from hand import Hand
from dealer import Dealer


def main() -> None:
    # Creates two Hand objects representing both player and computer
    player: Hand = Hand()
    computer: Hand = Hand()

    play_new_game: bool = True  # Loop flag that determines if a new game should be played
    while play_new_game:
        # Creates a Dealer object, passes both players (Hand objects) as arguments
        dealer: Dealer = Dealer(player=player, computer=computer)

        continue_game: bool = True  # Loop flag that determines if current game should continue
        while continue_game:
            # Deal one more card if current total player card value is less than 21 and player wants one more. Else the game concludes.
            if player.get_value() < 21:
                dealer.print_current_hands()
                if py.inputYesNo("\nOne more card? (y/n): ") == "yes":
                    dealer.deal_player()
                    dealer.deal_computer()
                else:
                    continue_game = False
            else:
                continue_game = False
        dealer.conclude_game()

        # "Clears" the terminal and resets the game if the player wants one more game. Else exits the game.
        if py.inputYesNo("\nDo you want to play another game? (y/n): ") == "yes":
            print("\n" * 15)
            dealer.reset_game()
        else:
            print("\nThank you for playing Tjugoett!\n")
            play_new_game = False


if __name__ == "__main__":
    main()
