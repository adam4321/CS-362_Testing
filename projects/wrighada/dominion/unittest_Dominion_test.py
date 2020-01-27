"""
Created on Thurs Jan 16 2020

@author: Adam Wright

Unit test file for dominion game
"""

from unittest import TestCase
import Dominion
import testUtility
import random


class TestCard(TestCase):
    def setUp(self):
        # Set Up Values for the tests
        player_names = testUtility.getPlayerNames()
        self.players = testUtility.getPlayers(player_names)
        # number of curses and victory cards
        self.nV = testUtility.getnV(self.players)
        self.nC = testUtility.getnC(self.players)
        self.box = testUtility.getBoxes(self.nV)
        supply_order = testUtility.getSupplyOrder()
        self.boxlist = testUtility.getBoxList(self.box)
        random.shuffle(self.boxlist)
        self.random10 = testUtility.getRandom10(self.boxlist)
        self.supply = testUtility.getSupply(self.box, self.random10)
        self.supply = testUtility.getDefaultSupply(self.supply, self.players, self.nV, self.nC)
        trash = []
        self.player = Dominion.Player('Annie')

    # def test_init(self):
    #     self.setUp()
    #     actions = 2
    #     cards = 8
    #     buys = 6
    #     coins = 3

    def test_init(self):
        self.setUp()
        cost = 1
        buypower = 5

        card = Dominion.Coin_card(self.player.name, cost, buypower)

        self.assertEqual

    def test_use(self):
        pass
