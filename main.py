# -*- coding: utf-8 -*-
"""
Main file that triggers the game Regenwormen. The instance of the game initiates players that can make moves. 

Created on Sun Dec 29 21:36:14 2024

@author: MauritsvandenOeverPr
"""
from player import Player
from regenwormen import Regenwormen

def main():
    #player1 = player()
    #player1.turn(8)
    #player1.turn()
    # print(player1.current_worms)
    test = Regenwormen()
    for i in test.list_of_players:
        print(i.playername)

if __name__ == "__main__":
    main()   