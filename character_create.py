import time
class Character:
    def __init__(self, name, arch, hp, attack):
        self.name = name
        self.arch = arch
        self.hp = hp
        self.attack = attack
        


def main():
    arch_choices = ["warrior", "wizard", "paladin", "berserk"]
    name = input("What is your name: ")
    time.sleep(.8)
    print(f"Great to meet you {name}")
    time.sleep(.5)
    arch_decision = ""
    while arch_decision.lower() not in arch_choices:
        arch_decision = input("\n\n\nWhat type of character would you like to be:\nWarrior\nWizard\nPaladin\nBerserk\n")
    character = Character(name, arch_decision, 10, 10)
    print(character.attack)

    return 0

main()
