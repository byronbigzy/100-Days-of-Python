import random

'''
Rules:
2-10 are worth their face value.
J, Q, K are worth 10.
A is worth 1 or 11, whichever makes a better hand.
The hand value is the sum of the card values. The hand value cannot exceed 21.
The player and dealer are each dealt two cards. The player can see one of the dealer's cards.
The player can choose to "hit" (take another card) or "stand" (end their turn).
The dealer must hit until their hand value is 17 or higher.
Assume that we have an infinite cards.

Checklist:
Deal both user and computer 2 cards each.
Detect when computer or user has blackjack (a hand value of 21 with the first two cards).
If computer gets blackjack, then the user loses (even if the user also has blackjack). If the user gets blackjack and the computer doesn't, then the user wins.
Calculate the user's and computer's scores based on their card values.
If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
Reveal computer's first card to the user.
Game ends immeditetly when the user score goes over 21 or if the user or computer gets a blackjack.
Ask the user if they want to get another card.
Once the user is done and no longer wants to draw anymore card, let the computer play. The computer should keep drawing cards unless their score goes over 16
Compare user and computer scores and see if it's a win, loss , or draw
Print out the player's and the computer's final hand and their scores at the end of the game.
'''

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

playerCards = []
dealerCards = []
playerScore = 0
dealerScore = 0

def deal_card(hand):
    card = random.choice(cards)
    hand.append(card)

# Game Start

# Deal User and Dealer 2 Cards Each
deal_card(playerCards)
deal_card(playerCards)

deal_card(dealerCards)
deal_card(dealerCards)

# First Loop
while playerScore < 21 and dealerScore < 21:
    # Calculate User and Computers Scores
    playerScore = sum(playerCards)
    dealerScore = sum(dealerCards)

    # Does the user or computer have blackjack?
    if dealerScore == 21:
        print("The dealer has blackjack! They win!")
        break
    if playerScore == 21:
        print("The player has blackjack! They win!")
        break

    # Check for ace and adjust score
    while playerScore > 21:
        if 11 in playerCards:
            playerScore = sum(playerCards)
            if playerScore > 21: 
                playerCards.remove(11)
                playerCards.append(1)
            else:
                break

    print(f"Your cards: {playerCards}, Your current score: {playerScore}")
    print(f"Dealer's cards: {dealerCards}")
    print(f"Dealer's first card: {dealerCards[0]}")
    choice = input("Would you like to draw another card? 'y' or 'n': ")

    if choice.lower() == 'y':
        deal_card(playerCards)
        playerScore = sum(playerCards)
        # Check for ace and adjust score
        while playerScore > 21 and 11 in playerCards:
            playerCards.remove(11)
            playerCards.append(1)
            playerScore = sum(playerCards)
        if playerScore > 21:
            break
    elif choice.lower() == 'n':
        break

# Dealer's turn
while dealerScore < 17 and playerScore <= 21:
    deal_card(dealerCards)
    dealerScore = sum(dealerCards)
    while dealerScore > 21:
        if 11 in dealerCards:
            dealerScore = sum(dealerCards)
            if dealerScore > 21: 
                dealerCards.remove(11)
                dealerCards.append(1)
            else:
                break

# Final Results
# Recalculate scores in case they changed
playerScore = sum(playerCards)
dealerScore = sum(dealerCards)

print(f"Your final hand: {playerCards}, Your final score: {playerScore}")
print(f"Dealer's final hand: {dealerCards}, Dealer's final score: {dealerScore}")

if playerScore > 21:
    print("You went over 21. You lose!")
elif dealerScore > 21:
    print("Dealer went over 21. You win!")
elif playerScore > dealerScore:
    print("You win!")
elif playerScore < dealerScore:
    print("You lose!")
else:
    print("It's a draw!")