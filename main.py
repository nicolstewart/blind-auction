
from art import logo
print(logo)

# new function for finding highest bidder
def highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

#ensuring dictionary is empty
bids ={}
continue_bidding = True

while continue_bidding:
    user_name = input("What is your name? ")
    user_bid = int(input("What is your bid?: $"))
    bids[user_name] = user_bid
    new_bid = input("Are there any other bidders? Type yes or no\n").lower()
    if new_bid == "no":
        continue_bidding = False
        highest_bidder(bids)
    elif new_bid == "yes":
        print("\n" *20)



