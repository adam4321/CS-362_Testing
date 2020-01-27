"""
Created on Thurs Jan 22 2020

@author: Adam Wright

Unit test file for dominion game
"""

from unittest import TestCase
import Dominion
import testUtility
import random


class TestCard(TestCase):
    def setUp(self):
        # Set Up Test Utility Values
        player_names = testUtility.getPlayerNames()
        self.players = testUtility.getPlayers(player_names)
        # number of curses and victory cards
        self.nV = testUtility.getnV(self.players)
        self.nC = testUtility.getnC(self.players)
        self.box = testUtility.getBoxes(self.nV)
        self.supply_order = testUtility.getSupplyOrder()
        self.boxlist = testUtility.getBoxList(self.box)

        self.random10 = testUtility.getRandom10(self.boxlist)
        self.supply = testUtility.getSupply(self.box, self.random10)
        self.supply = testUtility.getDefaultSupply(self.supply, self.players, self.nV, self.nC)
        self.trash = []
        self.player = Dominion.Player('Annie')

        # Initialize Woodcutter action card data
        self.name = "Woodcutter"
        self.cost = 3
        self.actions = 0
        self.cards = 0
        self.buys = 1
        self.coins = 2
        # Instantiate a Woodcutter Action card
        self.Woodcutter_card = Dominion.Woodcutter()

    # Action card init test
    def test_init(self):
        # Verify that the properties are correct
        self.assertEqual(self.name, self.Woodcutter_card.name)
        self.assertEqual(self.cost, self.Woodcutter_card.cost)
        self.assertEqual(self.actions, self.Woodcutter_card.actions)
        self.assertEqual(self.cards, self.Woodcutter_card.cards)
        self.assertEqual(self.buys, self.Woodcutter_card.buys)
        self.assertEqual(self.coins, self.Woodcutter_card.coins)

    def test_use(self):
        # Instantiate
        self.Woodcutter_card.use(self.player.name, self.trash)