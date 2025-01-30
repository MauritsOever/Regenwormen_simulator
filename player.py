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
        turn_active = True
        available_dice = 8
        dice_set_aside = []
        
        while turn_active:
            dice_rolled = self.roll(available_dice)
            
            print(f"You rolled {dice_rolled}")
            time.sleep(1)
            # add a check to see if you can choose a number or not-------------------------------------------------------------
            nr_set_aside = str(input("Which number do you choose to set aside? "))
            if nr_set_aside != "worm" and nr_set_aside != "Worm":
                nr_set_aside = int(nr_set_aside)
            
            if type(nr_set_aside) == str:
                nr_set_aside = "Worm"
            
            for die in dice_rolled:
                if die == nr_set_aside:
                    dice_set_aside += [die]
            
            available_dice = 8 - len(dice_set_aside)
            
            time.sleep(1)
            points_in_hand = 0
            for i in dice_set_aside:
                if i == "Worm":
                    points_in_hand += 5
                else:
                    points_in_hand += i
                    
            print(f"You're currently holding the following dice: {dice_set_aside}, giving a total of {points_in_hand} points.")
            action = input("Do you want to roll, take a stone or steal one from another player? ")
            print(f"You chose {action}.")
            
            if action == "steal" or action == "Steal":
                turn_active = False
                pass # figure out how to handle. maybe change attribute in player and take from initiating next turn
            elif action == "take" or action == "Take":
                taken_stone = input("Which stone do you want to take?")
                self.current_stack += [int(taken_stone)] #add a try except statement
                turn_active = False
            # roll, choose dice, choose to roll after (then repeat w less dice) or choose a stone
            
            
        return
        
    def roll(self, available_dice):
        rolled_dice = list(np.random.randint(1,7,available_dice)) #random array of ints with length available dice
        for i in range(len(rolled_dice)):
            rolled_dice[i] = int(rolled_dice[i])
            if rolled_dice[i] == 6:
                rolled_dice[i] = "Worm"
        return rolled_dice
        
    def take_stone(self, stone_number):
        pass
    
    def steal_stone(self, stone_number, player_number): #subject to change
        pass
    
    def strikeout(self):
        # return stone
        pass
    