import time
from char_moves import Move, characterMoves


class Character:
    def __init__(self, name, arch, hp, attack, moves):
        self.name = name
        self.arch = arch
        self.hp = hp
        self.attack = attack
        self.moves = moves

        


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
        moves = characterMoves("warrior")
        character = Character(name, arch_decision, 20, 10, moves)
    elif arch_decision == "wizard":
        moves = characterMoves("wizard")
        character = Character(name, arch_decision, 10, 20, moves)
    elif arch_decision == "paladin":
        moves = characterMoves("paladin")
        character = Character(name, arch_decision, 15, 15, moves)
    elif arch_decision == "berserk":
        moves = characterMoves("berserk")
        character = Character(name, arch_decision, 10, 20, moves)


   # print(character.arch, character.attack, [i.name for i in character.moves])
    

    return character


