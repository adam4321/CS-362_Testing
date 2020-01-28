"""
Created on Thurs Jan 22 2020

@author: Adam Wright

Unit test file for dominion game
"""

from unittest import TestCase
import Dominion
import testUtility


class TestCard(TestCase):
    def setUp(self):
        # Set Up Test Utility Values
        self.trash = []
        self.player = Dominion.Player('Annie')

        # Initialize action card props
        self.name = "Feast"
        self.cost = 4
        self.actions = 0
        self.cards = 0
        self.buys = 0
        self.coins = 0

        # Instantiate a Feast Action card
        self.Feast_card = Dominion.Feast()

    def test_init(self):
        self.setUp()

        # Verify that the properties are correct
        self.assertEqual(self.name, self.Feast_card.name)
        self.assertEqual(self.cost, self.Feast_card.cost)
        self.assertEqual(self.actions, self.Feast_card.actions)
        self.assertEqual(self.cards, self.Feast_card.cards)
        self.assertEqual(self.buys, self.Feast_card.buys)
        self.assertEqual(self.coins, self.Feast_card.coins)

    def test_use(self):
        self.setUp()

        # Only Feast card in hand
        self.player.hand.clear()
        self.player.hand.append(self.Feast_card)

        # Call method
        self.Feast_card.use(self.player, self.trash)

        # Verify that card can be trashed
        self.assertEqual(self.trash[0], self.Feast_card)

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


class TestPlayer(TestCase):
    def setUp(self):
        # Instantiate player
        self.player = Dominion.Player('Annie')

        # Clear the player's balance and deck
        self.player.balance = 0
        self.player.deck.clear()
        self.player.hand.clear()
        self.player.hold.clear()
        self.player.discard.clear()
        self.player.aside.clear()
        self.player.hold.clear()

    def test_action_balance(self):
        self.setUp()

        # Create Village action card (actions prop = 2)
        self.player.deck = [Dominion.Village()]

        # Call the method
        test_balance = self.player.action_balance()

        # Test that balance (0 - 1 + 2 = 1 * 70 = 70)
        self.assertEqual(test_balance, 70)

    def test_calcpoints(self):
        self.setUp()

        # Victory card Province points = 6 && Gardens = 0
        self.player.deck = [Dominion.Province()] * 2 + [Dominion.Gardens()]

        # Call the method
        point_total = self.player.calcpoints()

        # Test that balance = 12
        self.assertEqual(point_total, 12)

    def test_draw(self):
        self.setUp()

        # Store the state of the hand
        local_hand = self.player.hand

        # Call the method with no arguments
        self.player.draw()

        # Test default arg dest == self.hand
        self.assertEqual(local_hand, self.player.hand)

        # Call method with empty hand
        test_discard = self.player.discard
        self.player.deck.clear()
        self.player.draw()

        # Test second if which assigns discard to deck
        self.assertEqual(test_discard, self.player.deck)

        # Assign a new deck
        self.player.deck = [Dominion.Province()] * 2 + [Dominion.Gardens()]
        test_sub0 = self.player.deck[0]

        # Call the method
        test_draw = self.player.draw()

        # Test the 3rd if condition
        self.assertEqual(test_sub0, test_draw)

    def test_cardsummary(self):
        self.setUp()

        # Set up the player deck and it's summary
        self.player.deck = [Dominion.Province()] * 2 + [Dominion.Gardens()]
        summary_guess = {"Province": 2, "Gardens": 1, 'VICTORY POINTS': 12}

        # Call the method
        test_summary = self.player.cardsummary()

        # Test that the method returns the correct summary
        self.assertEqual(summary_guess, test_summary)


class TestGame(TestCase):
    def setUp(self):
        # Get player names
        self.player_names = testUtility.getPlayerNames()

        # number of curses and victory cards
        self.nV = testUtility.getnV(self.player_names)
        self.nC = testUtility.getnC(self.player_names)

        # Get box
        self.box = testUtility.getBoxes(self.nV)

        # Get supply order
        self.supply_order = testUtility.getSupplyOrder()

        # Pick 10 cards from box to be in the supply.
        self.boxlist = testUtility.getBoxList(self.box)
        self.random10 = testUtility.getRandom10(self.boxlist)
        self.supply = testUtility.getSupply(self.box, self.random10)

        # The supply always has these cards
        self.supply = testUtility.getDefaultSupply(self.supply, self.player_names, self.nV, self.nC)

        # initialize the trash
        self.trash = []

        # Construct the Player objects
        self.players = testUtility.getPlayers(self.player_names)

        # Instantiate player
        self.player = Dominion.Player('Annie')

    def test_gameOver(self):
        self.setUp()

        # Call method with province cards
        game_state = Dominion.gameover(self.supply)

        # Test the game continues by returning false
        self.assertEqual(game_state, False)

        # Clear out province cards
        self.supply.clear()

        # Call method without province cards
        game_state = Dominion.gameover(self.supply)

        # Test that the game ends by returning true

        self.assertEqual(game_state, True)
