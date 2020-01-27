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
        # Number of curses and victory cards
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

    # Action card init test
    def test_init(self):
        # Initialize Feast action card data
        self.setUp()
        self.name = "Feast"
        self.cost = 4
        self.actions = 0
        self.cards = 0
        self.buys = 0
        self.coins = 0

        # Instantiate a Feast Action card
        self.Feast_card = Dominion.Feast()

        # Verify that the properties are correct
        self.assertEqual(self.name, self.Feast_card.name)
        self.assertEqual(self.cost, self.Feast_card.cost)
        self.assertEqual(self.actions, self.Feast_card.actions)
        self.assertEqual(self.cards, self.Feast_card.cards)
        self.assertEqual(self.buys, self.Feast_card.buys)
        self.assertEqual(self.coins, self.Feast_card.coins)

    def test_use(self):
        self.setUp()
        # Instantiate a Feast Action card
        self.Feast_card = Dominion.Feast()
        self.use_trash = []
        self.player.hand.clear()
        self.player.hand.append(self.Feast_card)

        self.Feast_card.use(self.player, self.use_trash)

        # Verify that card can be trashed
        self.assertEqual(self.use_trash[0], self.Feast_card)
        # Verify that card is not still in the hand
        with self.assertRaises(ValueError):
            self.assertEqual(self.player.hand.index(self.Feast_card), self.Feast_card)

    def test_augment(self):
        self.setUp()
        # Set player props to 0
        self.player.actions = 0
        self.player.buys = 0
        self.player.purse = 0

        # Set card props to 1
        self.Feast_card = Dominion.Feast()
        self.Feast_card.actions = 1
        self.Feast_card.buys = 1
        self.Feast_card.coins = 1

        # Call method
        self.Feast_card.augment(self.player)

        # Verify the props are incremented
        self.assertEqual(self.player.actions, 1)
        self.assertEqual(self.player.buys, 1)
        self.assertEqual(self.player.purse, 1)
