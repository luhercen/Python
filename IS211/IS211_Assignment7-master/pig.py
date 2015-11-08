#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""is211 Assignment 7, pig game """

import random
import sys


class Die(object):

        def __init__(self):
            self.value = int()
		
        def roll(self):
            self.value = random.randint(1,6)


class Player(object):

        def __init__(self):

            self.scorecount = 0
            self.roll = True
            self.hold = False
            self.turntime = False
	
        def deciding(self):

            decision = raw_input('%s: Would you like to Hold or Roll ? (h/r)?' % self.name)
            decision = str(decision)

            if decision != "h" or "r":
                print "wrong input, enter again your decision"
                self.deciding

            else:
                if decision == 'h':
                    self.hold = True
                    self.roll = False
			
                elif decision == 'r':
                    self.hold = False
                    self.roll = True
		
		
class Game(object):

	def __init__(self,player1,player2,die):

		self.player1 = player1
		self.player1.score = 0
		self.player1.name = "Player 1"
		
		self.player2 = player2
		self.player2.score = 0
		self.player2.name = "Player 2"

		self.score_per_turn = 0
		self.die = Die()


		
		coinplay = random.randint(1,2)

		if coinplay == 1:

			self.current_player = player1
			print "Coin result in player 1 decision, player 1 can begin"
			
		elif coinplay == 2:
		
			self.current_player = player2
			print "Coin result in player 1 decision, player 2 can begin "
			
		else:
			print "no one's side selection, flip again"
			

		self.turn()
		
		
	def newturn(self):

		self.score_per_turn = 0	
		if self.player1.score >= 100:

			print "End of the game player 1 wins!"
			print "Final player 1 score:",self.player1.score
			self.gamends()
			main()
			
		elif self.player2.score >= 100:

			print "End of the game player 2 wins!"
			print "Final player 2 Score:",self.player2.score
			self.gamends()
			main()
			
		else:
			if self.current_player == self.player1:
				self.current_player = self.player2
			elif self.current_player == self.player2:
				self.current_player = self.player1
			else:
				print "error , try flipping again"

			print "Flip the coin for a new turn player : ", self.current_player.name
			self.turn()

		
	def turn(self):

		print "Current Player 1 Score:", self.player1.score				
		print "Current Player 2 Score:", self.player2.score
		
		self.die.roll()
		
		if(self.die.value == 1):

			print "you got 1 , points = 0 !"
			self.score_per_turn = 0
			self.newturn()
			
		else:

			self.score_per_turn += self.die.value
			print "Dice shows you a:",self.die.value
			print "Your current score is:", self.score_per_turn
			
			self.current_player.deciding()
			if(self.current_player.hold == True and self.current_player.roll == False):
				self.current_player.score = self.current_player.score + self.score_per_turn
				self.newturn()
			elif(self.current_player.hold == False and self.current_player.roll == True):
				self.turn()
				
	def gamends(self):
		self.player1 = None
		self.player2 = None
		self.die = None
		self.score_per_turn = None
	

def main():

        start = raw_input("Would you like to start a new game?, Yes(Y) or No(N)?")
        if start == 'Y':
            player1 = Player()
            player2 = Player()
            die = Die()					
            newgame = Game(player1,player2,die)

        elif start == 'N':
            print "Ok bye"
            sys.exit()

        else:
            print "Type only (Y) or (N)"


if __name__ == '__main__':
    main()
