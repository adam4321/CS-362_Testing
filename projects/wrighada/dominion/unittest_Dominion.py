"""
Created on Thurs Jan 16 2020

@author: Adam Wright

Unit test file for dominion game
"""

import testUtility
import random
import Dominion

class TestCard:
    def setUp(self):
        # Set Up Vales for the tests
        player_names = testUtility.getPlayerNames()
        players = testUtility.getPlayers(player_names)
        # number of curses and victory cards
        nV = testUtility.getnV(player_names)
        nC = testUtility.getnC(player_names)
        box = testUtility.getBoxes(nV)
        supply_order = testUtility.getSupplyOrder()
        boxlist = testUtility.getBoxList(box)
        random.shuffle(boxlist)
        random10 = testUtility.getRandom10(boxlist)
        supply = testUtility.getSupply(box, random10)
        supply = testUtility.getDefaultSupply(supply, player_names, nV, nC)
        trash = []

    def test_init(self):
        self.setUp()
        cost = 1
        buyPower = 5

    def test_use(self):
        pass
