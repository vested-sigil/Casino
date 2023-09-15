import random
from TarotMajor import major_arcana_cards
from TarotMajor import major_arcana_interpretations  # Import Major Arcana interpretations
from TarotMinor import minor_arcana_cards
from TarotMinor import minor_arcana_interpretations  # Import Minor Arcana interpretations

# Combine Major Arcana and Minor Arcana card lists
tarot_deck = list(major_arcana_interpretations.keys()) + list(minor_arcana_interpretations.keys())
tarot_cards = list(major_arcana_cards.keys()) + list.minor_arcana_cards
deck =tarot_deck
cards = tarot_cards
# Create a function to shuffle and deal the tarot deck
def shuffle_and_deal(deck):
    random.shuffle(deck)
    return deck

# Create a function to draw a specified number of cards from the deck
def draw_cards(deck, num_cards):
    if num_cards <= len(deck):
        drawn_cards = deck[:num_cards]
        del deck[:num_cards]
        return drawn_cards
    else:
        return "Not enough cards in the deck to draw."

# Create a function to interpret a single card
def interpret_card(card, orientation, major_arcana, minor_arcana):
    if card in major_arcana:
        return major_arcana[card][orientation]
    elif card in minor_arcana:
        return minor_arcana[card][orientation]
    else:
        return ["Invalid card."]

# Create a function to interpret a list of cards
def interpret_card_list(cards, orientation, major_arcana, minor_arcana):
    interpretations = []
    for card in cards:
        interpretation = interpret_card(card, orientation, major_arcana, minor_arcana)
        interpretations.append(f"{card} ({orientation.capitalize()}): {', '.join(interpretation)}")
    return interpretations

# Create a function for a one-card tarot reading
def hit_me():
    tdeck = shuffle_and_deal(deck)
    drawn_card = draw_cards(tdeck, 1)[0]
    card.orientation = random.choice(card.orientation)
    if card in major_arcana:
        interpretation = interpret_card(major_arcana[card][orientation])
        return interpretation
    elif card in minor_arcana:
    	interpretation = interpret_card(minor_arcana[card][orientation])
    	return interpretation
    else:
        return ["Invalid card."]
    
# Create a function for a three-card spread tarot reading
def spreadhand():
    hit_me()
    hit_me()
    hit_me()
    return interpretations

# Add more functions for different tarot spreads as needed

def get_card_of_the_day():
    # Randomly select a card from the deck
    card = random.choice(tarot_deck)
    
    # Generate an interpretation for the card (you can use your existing interpretation logic here)
    interpretation = get_minor_arcana_interpretation(card, 'upright')
    
    return card, interpretation

# Example usage
if __name__ == "__main__":
    card, interpretation = get_card_of_the_day()
    print(f"Card of the Day: {card}")
    print("Interpretation:")
    for line in interpretation:
        print(f"- {line}")
