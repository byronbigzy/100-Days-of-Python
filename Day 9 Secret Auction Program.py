import os

logo = ''

def find_highest_bidder(bids_dict):
    winner = ""
    highest_bid = 0
    for bidder in bids_dict:
        bid_amount = bids_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f"The winner of the auction is {winner}, with the amount of ${highest_bid}.")

bids = {}

continuing = True

while continuing:
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")

    bids[name] = int(bid)

    cont = input("Are there any more participants? 'Yes' or 'No': ")

    if cont.lower() == 'no':
        continuing = False
        find_highest_bidder(bids)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
