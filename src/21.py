import random

def main():
    print("Welcome to the game of 21!")
    print("The goal of the game is to get as close to 21 as possible without going over.")
    print("Numbered cards are worth their face value, face cards are worth 10, and aces are worth 1 or 11.")
    print("You will be playing against the dealer. Good luck!\n")

    # initialize deck
    deck = get_deck()
    random.shuffle(deck)

    # initialize hands
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # player's turn
    while True:
        print(f"Your hand: {player_hand} ({get_hand_value(player_hand)})")
        if get_hand_value(player_hand) > 21:
            print("Bust! You lose.")
            return
        print(f"Dealer's hand: [{dealer_hand[0]}, ?]")
        choice = input("Do you want to hit or stand? ").lower()
        if choice == "hit":
            player_hand.append(deck.pop())
        elif choice == "stand":
            break
        else:
            print("Invalid choice. Please enter hit or stand.")

    # dealer's turn
    while get_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    # determine winner
    player_value = get_hand_value(player_hand)
    dealer_value = get_hand_value(dealer_hand)
    print(f"\nYour hand: {player_hand} ({player_value})")
    print(f"Dealer's hand: {dealer_hand} ({dealer_value})")
    if dealer_value > 21:
        print("Dealer bust! You win.")
    elif player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("You lose.")
    else:
        print("Draw.")

def get_deck():
    deck = []
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = list(range(1, 10)) + ["Jack", "Queen", "King", "Ace"]
    for suit in suits:
        for value in values:
            deck.append((value, suit))
    return deck

def get_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        if card[0] == "Ace":
            num_aces += 1
            value += 11
        elif card[0] in ["Jack", "Queen", "King"]:
            value += 10
        else:
            value += card[0]
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    return value

if __name__ == "__main__":
    main()
