from logo import logo

print(logo)
bids = {}


def findHighestBidder(bid):
    max = -1
    highestBidder = ""
    for bidder in bid:
        if max < bid[bidder]:
            max = bid[bidder]
            highestBidder = bidder
    return highestBidder


while True:
    name = str(input("what's the name of the bidder: "))
    price = int(input("By how much he will bid: "))
    if price >= 0:
        bids[name] = price
    else:
        print("the Bid cant be negative")
    flag = str(input("Are there are any other bidders? Type 'yes' or 'no' : "))
    if flag == "no":
        break

highestBidder = findHighestBidder(bids)
if highestBidder == "":
    print("no one had bit")
else:
    print(f"The winner is {highestBidder} by the amount of bid $ {bids[highestBidder]}")
