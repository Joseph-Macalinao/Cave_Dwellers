from enemiesClass import Wolf, Orc, Goblin
from character_create import Character
from char_moves import characterMoves
import random


char = Character("berserk", 10, 10, characterMoves("berserk"))

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
	#move_dec = ""
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
				print(i, i.damage)
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
		elif character_choice.lower() == "run":
			run_chance = random.random()
			if run_chance <= .75:
				print("Run successful")
				break
			else:
				print("Run unsuccessful")
				continue
	
		elif character_choice.lower() == "item":
			if len(character.inventory) > 0:
				for i in character.inventory:
					print(i)



#char = Character("Joseph", "berserk", 10, 10, characterMoves("berserk"))
battle_init()	
