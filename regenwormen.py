# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 21:43:52 2024

@author: MauritsvandenOeverPr
"""
from player import Player

class Regenwormen:
    def __init__(self):
        self.current_available_stones = [i for i in range(21,37)]
        self.list_of_players = []
        # that's kind of it right??
        
        print("Welcome to Regenwormen!")
        player_amount = int(input("How many players are joining this game? "))
        bots_amount = int(input("How many bots are joining this game? "))
        
        for i in range(player_amount - bots_amount): # add human players
            player_name = input(f"Player {i+1}, what is your name? ")
            self.list_of_players += [Player(playername = player_name)]
        
        for i in range(bots_amount): # add bots
            self.list_of_players += [Player(bot=True, playername= "bot"+str(i+1))]
          
        self.active_game()
        return
        
        
    def determine_stealable_stones(self):
        list_of_stones = []
        for player in self.list_of_players:
            if len(player.current_stack) > 0:
                list_of_stones += [player.current_stack[-1]]
        return list_of_stones
    
    
    def active_game(self):
        """
        Initiates the active game loop. Will select a random player to start with.
        The loops over players and makes their turn. The game ends when all stones
        are taken or gone. 

        Returns
        -------
        None.

        """
        print("active game not yet implemented!")
        
        # runs the game, chooses a random player to start the game with
        # maybe loop something like
        # while game active:
            # turn player (current_available_stones, stones that you can steal), keep going until they take, steal or run out
            # if run out, decrease their stack, place it into the current_available_stones, flip highest one
            # if take, you need to change available stones, and add it to player.current_stack
            # if steal, you need to change the current_stack of one of the other players (simple loop to figure out which)
        pass
    