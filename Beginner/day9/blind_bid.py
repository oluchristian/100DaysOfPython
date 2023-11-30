from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program")

bidders_list = []
def add_details(username, bid_price):
  details = {"name": username, "bid": bid_price}
  bidders_list.append(details)
bidders = True
while bidders:
  usr_name = input("What is your name: ")
  bid = int(input("Type your bid: $"))
  add_details(username=usr_name, bid_price=bid)
  other_bidders = input("Are there any other bidders? Type yes or no")
  if other_bidders != 'yes':
    bidders = False
  clear()
print(bidders_list)
max = 0
highest_bid = ''
for item in bidders_list:
  if item['bid'] > max:
    max = item['bid']
    highest_bid = item['name']
print(f"{highest_bid} has the highest bid of {max}")
    