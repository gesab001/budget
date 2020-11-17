import json

file = open("shoppinglist.json", "r")
jsondata = json.load(file)

total = 0

while True:
 total = 0
 item = input("item: ")
 price = float(input("price: "))
 quantity = int(input("quantity: "))
 subprice = price * quantity
 jsondata["items"][item] = subprice

 with open("shoppinglist.json", "w") as outfile:
   json.dump(jsondata, outfile, indent=4)

 for item in jsondata["items"]:
  name = item
  price = jsondata["items"][item] 
  print(item, str(price))
  total = total + price
 print("total: ", total)
