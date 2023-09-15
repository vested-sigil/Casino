import TarotUtil  # Import your TarotUtil module

# Define constants for card orientations
Upright = 'upright'
Reversed = 'reversed'

class TarotSystem:
    def __init__(self):
        # Initialize the tarot deck and any other necessary variables
        self.tarot_deck = TarotUtil.tarot_deck

    def draw_cards(self, num_cards):
        # Draw a specified number of cards from the tarot deck
        return TarotUtil.draw_cards(self.tarot_deck, num_cards)

    def interpret_card(self, card, orientation):
        # Interpret a single card
        return TarotUtil.interpret_card(card, orientation)

    def one_card_reading(self, orientation):
        # Perform a one-card tarot reading
        return TarotUtil.one_card_reading(self.tarot_deck, orientation)

    def three_card_spread(self, orientation):
        # Perform a three-card spread tarot reading
        return TarotUtil.three_card_spread(self.tarot_deck, orientation)

    # You can add more tarot-related functions as needed here

if __name__ == "__main__":
    # Example usage of the TarotSystem
    tarot = TarotSystem()
    
    # Perform a one-card tarot reading and print the result
    card, interpretation = tarot.one_card_reading(Upright)
    print(f"Card Drawn: {card}")
    print("Interpretation:")
    for line in interpretation:
        print(f"- {line}")

