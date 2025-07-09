bedroom = ["Controller", "Charger", "Playstation", "Shoes", "Glasses" "Wallet" ]

travelBag = []

print("Pack Your Bag")
print("Enter the index of an item you'd like to move from your room to your bag.")
print("Type '100' when you are done packing.\n")
print("Your Bedroom Items")
for item in bedroom:
    print(item)


item =int(input("Index"))

while item != 100:
    travelBag.append(bedroom[item])
    print("\nYour Bedroom:")
    print(bedroom)
    print("\nYour Travel Bag:")
    print(travelBag)
    item = int(input("Itemb Index:"))

    print("\nYour finished luggage:")
    print(item)