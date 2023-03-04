import time
from char_moves import characterMoves


class Character:
    def __init__(self, arch, hp, attack, moves, gold=0):
        self.arch = arch
        self.hp = hp
        self.attack = attack
        self.moves = moves
        self.gold = gold
        self.inventory = []


def createCharacter():
    arch_choices = ["warrior", "wizard", "paladin", "berserk"]
    character = None
    arch_decision = ""
    while arch_decision.lower() not in arch_choices:
        arch_decision = input("What type of character would you like to be:\nWarrior\nWizard\nPaladin\nBerserk\n")
    arch_decision = arch_decision.lower()
    if arch_decision == "warrior":
        moves = characterMoves("warrior")
        character = Character(arch_decision, 20, 10, moves)
    elif arch_decision == "wizard":
        moves = characterMoves("wizard")
        character = Character(arch_decision, 10, 20, moves)
    elif arch_decision == "paladin":
        moves = characterMoves("paladin")
        character = Character(arch_decision, 15, 15, moves)
    elif arch_decision == "berserk":
        moves = characterMoves("berserk")
        character = Character(arch_decision, 10, 20, moves)
    # print(character.arch, character.attack, [i.name for i in character.moves])
    return character
