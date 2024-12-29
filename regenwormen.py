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
        