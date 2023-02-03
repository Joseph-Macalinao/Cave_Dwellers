#from character_create import Character
from fileManage import replace_line


def storeMessage():
    print("Welcome to the Crafty Badger, your hub for all items you will need on your adventure")
    file = open("storeAmount.txt", "r")



def initialize(character):
    file = open("storeAmount.txt", "r+")
    heal = file.readline()
    wu = file.readline()
    ma = file.readline()
    sus = file.readline()
    lineRep = 0
    store_items = {"Healing Potion": int(heal), "Weapon Upgrade": int(wu),
                   "More Armor": int(ma), "Single-Use Shield": int(sus)}

    print("What would you like to buy today (q) to exit")
    for i in store_items:
        print(f"{i}: {store_items[i] * 10} gold")

    bought = None
    while bought not in store_items:
        bought = input()
        if bought == 'q' or bought == 'Q':
            break
        if bought not in store_items:
            print("Please choose an appropriate item")
    if character.gold < store_items[bought]:
        print("You do not have enought gold for that item.")
    elif character.gold >= store_items[bought]:
        if bought == "Healing Potion":
            lineRep = 0
        elif bought == "Weapon Upgrade":
            lineRep = 1
        elif bought == "More Armor":
            lineRep = 2
        elif bought == "Single-Use Shield":
            lineRep = 3
        character.inventory.append(bought)
        character.gold -= store_items[bought]
        replace_line("storeAmount.txt", lineRep, str(store_items[bought] + 1))

    storeCont = input("Would you like to buy anyting else?\n")
    storeCont = storeCont.lower()
    if storeCont == "yes" or store_items == 'y':
        initialize()




initialize()
