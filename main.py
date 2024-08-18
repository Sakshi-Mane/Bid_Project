
def bid_winner(bidding_dictionary):
    winner = ""
    highest_bid=0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of {highest_bid}")


bid_dict = {}
should_continue = True
while should_continue:
    name = input("What is your name?\n")
    bid_price = int(input("How much is your bid? Rs \n"))
    bid_dict[name] = bid_price
    auction= input("Are there any other bidders? Type 'yes' or 'no' \n")
    if auction== "no":
        should_continue= False
        bid_winner(bid_dict)
    elif auction == "yes":
        print("\n " * 100)



