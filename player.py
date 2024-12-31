# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 21:43:31 2024

@author: MauritsvandenOeverPr
"""
import time
import numpy as np

class player:
    
    def __init__(self, bot=False, playername = "Maurits"):
        import time
        """
        Function that intiates the player object. A player can roll when it is
        their turn.

        Parameters
        ----------
        bot : Describes if the player is a bot or not. The default is False.

        Returns
        -------
        None.

        """
        self.playername = playername
        self.current_stack = [] #initiate a player with an empty stack
        self.current_worms = 0
        self.bot = bot
        
        return
    
    def set_current_worms(self):
        """
        Function that sets current worms after a roll.

        Returns
        -------
        None.

        """
        stone_stack_combos = {21:1, 22:1, 23:1, 24:1,
                              25:2, 26:2, 27:2, 28:2,
                              29:3, 30:3, 31:3, 32:3,
                              33:4, 34:4, 35:4, 36:4}
        
        current_worms = 0
        for stone in self.current_stack():
            current_worms += stone_stack_combos[stone]
            
        self.current_worms = current_worms
        return
    
    def turn(self, available_stones="full", stealable_stones=None):
        """
        When it is the player's turn their roll is intiated. 

        Parameters
        ----------
        available_stones : TYPE, optional
            DESCRIPTION. The default is "full".
        stealable_stones : TYPE, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        None.

        """
        if available_stones=="full":                    # filler statement, when actually running the
            available_stones= [i for i in range(21,37)] # game u need to pass always anyway
                                                        
        
        print(f"{self.playername}, it's your turn!")
        print("Rolling...")
        time.sleep(1)
        print("")
        rolled_dice = self.roll(8)
        print("You rolled ")
        turn_active = True
        available_dice = 8
        while turn_active:
            dice_rolled = self.roll(available_dice)
            
            print(f"You rolled {dice_rolled}")
            action = input("Do you want to take, steal or roll?")
            
            if action == "roll":
                chosen_number = int(input("Which number do you choose to set aside?")) #need to figure out how to add worm
                pass # continue loop and store what you chose
            elif action == "steal":
                pass # figure out how to handle. maybe change attribute in player and take from initiating next turn
            elif action == "take":
                taken_stone = input("Which stone do you want to take?")
                self.current_stack += [int(taken_stone)] #add a try loop
            # roll, choose dice, choose to roll after (then repeat w less dice) or choose a stone
            
            if available_dice == 0:
                self.strikeout()
                print("Too bad, no more dice option available")
                turn_active = False
        return
        
    def roll(self, available_dice):
        return np.random.randint(1,7,available_dice) #random array of ints with length available dice
        
    def take_stone(self, stone_number):
        pass
    
    def steal_stone(self, stone_number, player_number): #subject to change
        pass
    
    def strikeout(self):
        pass
    