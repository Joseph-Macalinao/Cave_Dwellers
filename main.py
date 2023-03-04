import time
from character_create import createCharacter
from userCreation import userCreation


def main():
    # Introduction to Cave Dwellers
    print("Hello!")
    time.sleep(2)
    print("Welcome to Cave Dwellers, an adventure game made for up\nand coming adventurers like yourself!")
    print("First things first, we need to get to know you a little bit.")
    # Creates User and Character Class
    userCreation()
    """
    created = createCharacter()
    file = open("characterStats.txt", "r+")
    file.write(created.name + "\n")
    file.write(created.arch + "\n")
    file.write(str(created.hp) + "\n")
    file.write(str(created.attack) + "\n")
    file.write(str(created.moves) + "\n")
    file.write(str(created.gold) + "\n")
    file.write(str(created.inventory) + "\n")
    """
    return

main()
