from enemiesClass import Wolf, Orc, Goblin
from character_create import Character
from char_moves import characterMoves
import random


char = Character("wizard", 10, 10, characterMoves("wizard"))

def battle_init():
	enemy_dec = random.random()
	if 0 < enemy_dec < .333:
		enemy_dec = Wolf()
	elif .333 < enemy_dec < .666:
		enemy_dec = Orc()
	elif .666 < enemy_dec:
		enemy_dec = Goblin()
	
	#print(enemy_dec.name, enemy_dec.health)
	battle(char, enemy_dec)


def move(attacked, move):
	pass




def battle(character, enemy):
	#for i in range(len(character.moves)):
	#	print(character.moves[i].name)
	char_hp = character.hp
	enem_hp = enemy.hp
	#print(type(enem_hp), type(char_hp))
	char_moves = {}
	fin_move = None
	move_dec = ""
	for i in character.moves:
		char_moves[i.name.lower()] = (i.damage, i.crit)
	#print(char_moves.keys())
	while(char_hp > 0 and enem_hp > 0):
		move_dec = ""
		print(enemy.name, enem_hp)
		character_choice = input("Would you like to:\nAttack\nEnchant\nItem\nRun\n")
		if character_choice.lower() == "attack":
			print("-----------------------")
			print("Moves:")
			for i in char_moves:
				print(i, ": Damage: ", char_moves[i][0])
			while move_dec not in char_moves.keys():
				move_dec = input("Move choice: ")
				if move_dec.lower() in char_moves:
					fin_move = (move_dec, char_moves[move_dec][0], char_moves[move_dec][1])
			crit_chance = random.random()
			if crit_chance <= fin_move[2]:
				print("Critical Hit!")
				enem_hp -= (2*fin_move[1])
			else:
				enem_hp -= fin_move[1]
			#print(enemy.name, enem_hp)
			if enem_hp <= 0:
				break
		elif character_choice.lower() == "run":
			run_chance = random.random()
			if run_chance <= .3:
				print("Run successful")
				break
			else:
				print("Run unsuccessful")
				
	
		'''elif character_chose.lower() == "item":
			if len(character.inventory) > 0:
				for i in character.inventory:
					print(i)'''
		print(f"The {enemy.name} attacks!")
		crit_chance = random.random()
		if crit_chance <= .2:
			print("They did critical damage!")
			char_hp -= (2*enemy.attack)
		else:
			char_hp -= enemy.attack
		if char_hp <= 0:
			print("You now have 0 health left!")
		else:
			print(f"You now have {char_hp} health left!")
		
	if enem_hp <= 0:
		print(f"Congrats! You beat the {enemy.name}. You get 10 gold!")
		character.gold += 10
		print(f"You now have {character.gold} gold")
	if char_hp <= 0:
		print(f"Oh no! You lost to the {enemy.name}! You lose 10 gold!")
		if character.gold <= 10:
			character.gold = 0
		else:
			character.gold -= 10
			print(f"Oh no! You lost to the {enemy.name}! You lose 10 gold!")
	


#char = Character("Joseph", "berserk", 10, 10, characterMoves("berserk"))
battle_init()	
