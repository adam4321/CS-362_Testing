# -*- coding: utf-8 -*-
"""
Created on Thurs Jan 16 2020

@author: Adam Wright

Initial test file without bugs
"""

import Dominion
import testUtility


# Get player names
player_names = testUtility.getPlayerNames()


# number of curses and victory cards
nV = testUtility.getnV(player_names)
nC = testUtility.getnC(player_names)


# Get box
box = testUtility.getBoxes(nV)


# Get supply order
supply_order = testUtility.getSupplyOrder()


# Pick 10 cards from box to be in the supply.
boxlist = testUtility.getBoxList(box)
random10 = testUtility.getRandom10(boxlist)
supply = testUtility.getSupply(box, random10)


# The supply always has these cards
supply = testUtility.getDefaultSupply(supply, player_names, nV, nC)


# initialize the trash
trash = []


# Construct the Player objects
players = testUtility.getPlayers(player_names)


# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)


# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)
