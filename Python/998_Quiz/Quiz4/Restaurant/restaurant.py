import random

restaurantlist = ["In-N-Out", "Arby's", "Cheescake Factory"]
InOutMenu = ["Double-Double Cheesburger", "Fries", "2 Gallon Specialty Coke"]
ArbyMenu = ["Beef Sandwich", "Grilled chicken sandwich", "Buffalo Roast Chicken Sandwich"]
ChesscakMenu = ["Carne Asada Steak Medallions", "Pro Cheesburger(Pro)", "Chicken Taquitos"]

restaurantchoice = input("Choose a restaurant - In-N-Out, Arby's, or Cheescake Factory")
print("Your restaurant is" + restaurantchoice)


if restaurantchoice == "In-N-Out":
    print(InOutMenu)
    print(random.choice(InOutMenu))
elif restaurantchoice == "Arby's":
    print(ArbyMenu)
    print(random.choice(ArbyMenu))
elif restaurantchoice == "Cheescake Factory":
    print(ChesscakMenu)
    print(random.choice(ChesscakMenu))
else: 
    print("That restaurant doesn't exist in this universe.")

