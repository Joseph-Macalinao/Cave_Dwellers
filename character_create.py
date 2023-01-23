import time
class Character:
    def __init__(self, name, arch, hp, attack):
        self.name = name
        self.arch = arch
        self.hp = hp
        self.attack = attack

        


def createCharacter():
    arch_choices = ["warrior", "wizard", "paladin", "berserk"]
    name = input("What is your name: ")
    time.sleep(.8)
    print(f"Great to meet you {name}")
    time.sleep(.5)
    arch_decision = ""
    while arch_decision.lower() not in arch_choices:
        arch_decision = input("\n\n\nWhat type of character would you like to be:\nWarrior\nWizard\nPaladin\nBerserk\n")
    arch_decision = arch_decision.lower()
    if arch_decision == "warrior":
        character = Character(name, arch_decision, 20, 10)
    elif arch_decision == "wizard":
        character = Character(name, arch_decision, 10, 20)
    elif arch_decision == "paladin":
        character = Character(name, arch_decision, 15, 15)
    elif arch_decision == "berserk":
        character = Character(name, arch_decision, 10, 20)


    print(character.arch, character.attack)
    

    return character


