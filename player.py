# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 21:43:31 2024

@author: MauritsvandenOeverPr
"""
import time
import numpy as np
import os

class Player:
    
    def __init__(self, bot=False, playername = "Maurits"):
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
    
    def turn(self, available_stones=[i for i in range(21,37)], stealable_stones=[]):
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
        action and information related to the action:
            "take", and the stone that needs to be taken from the common stack
            "steal", and which stone needs to be stolen
            "strikeout", and the current stack. from there you can figure out what to do with the common stack
        """
                                                        
        
        print(f"{self.playername}, it's your turn!")
        print("Rolling...")
        time.sleep(1)
        turn_active = True
        available_dice = 8
        dice_set_aside = []
        points_in_hand = 0
        
        while turn_active:
            print(f"Available stones on the table are {available_stones}")
            if len(stealable_stones) > 0:
                print(f"Stone available to steal are {stealable_stones}")
            
            dice_rolled = self.roll(available_dice)
            if all([die in dice_set_aside for die in dice_rolled]):
                print(f"You rolled {dice_rolled}.")
                print("You've struck out! Ending your turn...")
                if len(self.current_stack) > 0:
                    print("You have to hand in your last stone :(")
                return "strikeout", self.current_stack
            
            # add a check to see if you can choose a number or not-------------------------------------------------------------
            choosing_dice = True
            while choosing_dice:
                print(f"You rolled {dice_rolled}")
                time.sleep(1)
                
                nr_set_aside = str(input("Which number do you choose to set aside? "))
                if nr_set_aside != "worm" and nr_set_aside != "Worm":
                    try:
                        if 1 <= int(nr_set_aside) <= 5:
                            nr_set_aside = int(nr_set_aside)
                    except:
                        print("Invalid number added, please enter another number...")
                        continue
                
                if nr_set_aside in dice_set_aside:
                    print("You've already chosen this number, please choose another one!")
                    continue
                choosing_dice = False
                    
            
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
            
            action = None
            while action == None:
                print(f"You're currently holding the following dice: {dice_set_aside}, giving a total of {points_in_hand} points.")
                if points_in_hand >= available_stones[0] and points_in_hand in stealable_stones:
                    action = input("Do you want to roll, take a stone or steal one from another player? ")
                    print(f"You chose {action}.")
                    continue
                elif points_in_hand >= available_stones[0]:
                    action = input("Do you want to roll or take a stone?")
                    print(f"You chose {action}.")
                    continue
                elif points_in_hand in stealable_stones:
                    action = input("Do you want roll or steal a stone from another player? ")
                    print(f"You chose {action}.")
                    continue
                else:
                    print("You have to roll...")
                    action = "roll"
                    continue
                print("Invalid action, try again!")
            
            if action == "steal" or action == "Steal":
                turn_active = False
                stolen_stone = points_in_hand #can only steal when you have the correct number of points, and add the check later
                return "steal", stolen_stone
            
            elif action == "take" or action == "Take":
                taken_stone = input("Which stone do you want to take?")
                self.current_stack += [int(taken_stone)] #add a try except statement
                return "take", taken_stone
                turn_active = False
            
            os.system("cls")
                        
        return
        
    def roll(self, available_dice):
        rolled_dice = list(np.random.randint(1,7,available_dice)) #random array of ints with length available dice
        for i in range(len(rolled_dice)):
            rolled_dice[i] = int(rolled_dice[i])
            if rolled_dice[i] == 6:
                rolled_dice[i] = "Worm"
                
        return rolled_dice
    