import sys
import os
import random

class Player:
	def __init__(self, none):
	self.name = name
	self.maxhealth = 100
	self.health = maxhealth
	self.attack = 10
	self.gold = 0
	self.potions = 0

class Goblin:
	def _init_(self, none):
	self.name = name
	self.maxhealth = 50
	self.health = maxhealth
	self.attack = 5
	self.goldgain = 10
GoblinInGame = Goblin("Goblin")

class Zombie:
	def _init_(self, none):
	self.name = name
	self.maxhealth = 70
	self.health = maxhealth
	self.attack = 7
	self.goldgain = 15
ZombieInGame = Zombie("Zombie")

def main():
	print "Welcome to my game!"
	print "1. Start"
	print "2. Load"
	print "3. Exit"
	option = raw_input("-> ")
	if option == "1":
		start()
	elif option == "2":
		pass	
	elif option == "3":
		sys.exit()
	else:
		main()

def start():
	print "Hello, What is your name?"
	option = raw_input("->")
	global PlayerInGame
	PlayerInGame = Player(option)
	start1()

def start():
	print "Name: %s" % PlayerInGame.name
	print "Attack: %i" % PlayerInGame.attack
	print "Gold: %d" % PlayerInGame.gold
	print "Potions: %d" % PlayerInGame.gold
	print "Health: %i/%i" % (PlayerIG.health, PlayerIG.maxhealth)
	print "1. Fight"
	print "2. Store"
	print "3. Save"
	print "4. Exit"
	option = raw_input("-> ")
	if option == "1":
		prefight()
	elif option == "2":
		start()
	elif option == "3":
		pass()
	elif option == "4":
		sys.exit()
	else:
		start1():

def prefight():
	enemynum = random,randint(1, 2)
	if enemynum == 1
		enemy == GoblinInGame
	else:
		enemy = ZombieInGame
	fight()

def fight():
	print "%s      vs       %s" % (PlayerInGame.name, enermyname
	print %s's Health: %d/%d   %s's Health: %i/%i (PlayerInGame.name, PlayerInGame.health, PlayerInGame.maxhealth, enemy.name, enemy.health, enemy.maxhealth)
	print "Potions %i" % PlayerInGame.potions
	print "1. Attack"
	print "2. Drink Potion"
	print "3. Run
	option = raw_input(' ')
	if option == "1":
		attack()
	if option == "2":
		drinkpot()
	if option == "3":
		run()
	else fight

def attaack():
	PAttack = random.randint(PlayerInGame.attack / 2, PlayerInGame.attack)
	EAttack = random.randint(enemy.attack / 2, enemy.attack)
	if PAttack == PlayerInGame.attack / 2:
		print "You miss!"
	else
		enemy.health -= PAttack
		print "You deal %i damage!" % PAttack
	if enemy.health <=0:
		win()
	option = raw_input(' ')
	if EAttack == enemy.attack/2:
		print "The enemy missed"
	else:
		PlayerInGame.health -= EAttack
		print "The enemy deals %i damage"
	option = raw.input(' ')
	if PlayerInGame.health <= 0:
		dead()
	else:
		fight()
	
def drinkpot():
	if PlayerInGame.pots = 0:
		print "You don't have any potions!"
		option = raw_input(' ')
		fight()
	else:
		PlayerInGame.health == 50
		if PlayerInGame > PlayerInGame.maxhealth:
			PlayerInGame.health - PlayerInGame.maxhealth
		print "You drank a potion"
	option = raw_input(' ')

def run():
	runum = random.randint(1, 3)
	if runum == 1:
		print "You have successfully ran away!"
		option = raw_input(' ')
		start1()
	else:
		print "You failed to get away!"
		option = raw_input(' ')
		EAttack = random.randint(enemy.attack / 2, enemy.attack)
		if EAttack == enemy.attack/2:
			print "The enemy missed"
		else:
			PlayerInGame.health -= EAttack
			print "The enemy deals %i damage"
		option = raw.input(' ')
		if PlayerInGame.health <= 0:
			dead()
		else:
			fight()

def win():
	PlayerInGame.gold += enemy.goldgain
	enemy.health = enemy.maxhealth
	print "You have defeated the %s" % enemy.name
	print "You have found %i gold!" % enemy.goldgain
	option = raw_input(' ')
	start1()

def dead():
	print "You have died"
  option = raw_input(' ')

main()
