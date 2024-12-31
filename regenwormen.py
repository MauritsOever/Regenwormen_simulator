# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 21:43:52 2024

@author: MauritsvandenOeverPr
"""

class Regenwormen:
    def __init__(self, nr_of_players, nr_of_bots=0):
        self.current_available_stones = [i for i in range(21,37)]
        self.list_of_players = []
        # that's kind of it right??
        
    def determine_stealable_stones(self):
        list_of_stones = []
        for player in self.list_of_players:
            if len(player.current_stack) > 0:
                list_of_stones += [player.current_stack[-1]]
        return list_of_stones
    
    def active_game():
        # runs the game, chooses a random player to start the game with
        # maybe loop something like
        # while game active:
            # turn player (current_available_stones, stones that you can steal), keep going until they take, steal or run out
            # if run out, decrease their stack, place it into the current_available_stones, flip highest one
            # if take, you need to change available stones, and add it to player.current_stack
            # if steal, you need to change the current_stack of one of the other players (simple loop to figure out which)
        
        pass