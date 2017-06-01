import random
from time import sleep

player1=0
player2=0
choice='y'

print ("---------------------------")
print ("| SNAKES AND LADDERS GAME |")
print ("---------------------------")

"""This method checks for the presence of snakes or ladders in the board"""

def check_for_snakes_and_ladders(n):
	ladders = {4:14,9:31,28:84,18:45,21:42,51:67,71:91,78:97}
	snakes = {26:11,52:29,62:19,66:59,74:17,89:69,95:75,98:79}

	if n in ladders:
		print ("\nYipee!")
		print ("Its a ladder,Climb up\n")
		n = ladders[n]
	
	elif n in snakes:
		print ("\nOops!")
		print ("Its a snake,Come down\n")
		n = snakes[n]
	
	return n


"""This method generates random number for dice"""

def roll_dice():
	d =random.randint(1,6)
	print ("----------------------")
	print ("| Dice has shown :",d,"|")
	print ("----------------------")
	return d


"""This method display output for number less than 10 """

def s_out(player1,player2):
	print ("------------------")
	print ("| Current Status |")
	print ("------------------")

	print ("---------------- \t ----------------")
	print ("| PLAYER 1:",player1," |\t","| PLAYER 2:",player2," |")
	print ("---------------- \t ----------------")
	sleep(2)


"""This method display output for number greater than and equal to 10 """

def out(player1,player2):
	print ("------------------")
	print ("| Current Status |")
	print ("------------------")

	print ("-----------------\t -----------------")
	print ("| PLAYER 1:",player1," |\t","| PLAYER 2:",player2," |")
	print ("-----------------\t -----------------")
	sleep(2)


""" Main Game function """

def game():
	player1=0
	player2=0

	while True:
		print ("\n\nIts turn of PLAYER 1\n")
		player1 += roll_dice()
		player1 = check_for_snakes_and_ladders(player1)
		
		if player1>99:
			player1=100

		if(player1<10 or player2<10):
			s_out(player1,player2)
		else:
			out(player1,player2)
	
		if player1 > 99:
			print ("\n---------------------------------")
			print ("| Winner of the game is player1 |")
			print ("---------------------------------")
			break

		print ("\n\nIts turn of PLAYER 2\n")
		player2 += roll_dice()
		player2 = check_for_snakes_and_ladders(player2)
		
		if player2>99:
			player2=100

		if(player1<10 or player2<10):
			s_out(player1,player2)
		else:
			out(player1,player2)

		if player2 > 99:
			print ("\n---------------------------------")
			print ("| Winner of the game is player2 |")
			print ("---------------------------------")
			break

	print ("-------------")
	print ("| GAME OVER |")
	print ("-------------")


""" Start Here"""

while(choice=='y'):
	game()
	choice=input('DO you want to play again(y/n): ')
