import unittest
from camel_cards import *

# Redefining the tests
class TestCardCounterMethods(unittest.TestCase):
    def setUp(self):
        self.card_counter = CardCounter()

    def test_add_new_card(self):
        self.card_counter.add('A')
        self.assertEqual(self.card_counter.d, {'A': 1})

    def test_add_existing_card(self):
        self.card_counter.add('A')
        self.card_counter.add('A')
        self.assertEqual(self.card_counter.d, {'A': 2})



class TestDetermineHandStrength(unittest.TestCase):
    def test_full_house_true(self):
        hand = 'AAABB'
        self.assertEqual(Rank.FULL_H, determine_hand_strength(hand))

    def test_full_house_false(self):
        hand = 'AAABC'
        self.assertNotEqual(Rank.FULL_H, determine_hand_strength(hand))

    def test_three_of_a_kind_true(self):
        hand = 'AAABK'
        self.assertEqual(Rank.THREE_OAK, determine_hand_strength(hand))

    def test_three_of_a_kind_false(self):
        hand = 'AABCD'
        self.assertNotEqual(Rank.THREE_OAK, determine_hand_strength(hand))

    def test_two_pair_true(self):
        hand = 'AABBC'
        self.assertEqual(Rank.TWO_PAIR, determine_hand_strength(hand))

    def test_two_pair_false(self):
        hand = 'AABCD'
        self.assertNotEqual(Rank.TWO_PAIR, determine_hand_strength(hand))

    def test_one_pair_true(self):
        hand = 'AABCD'
        self.assertEqual(Rank.ONE_PAIR, determine_hand_strength(hand))

    def test_one_pair_false(self):
        hand = 'ABCDE'
        self.assertNotEqual(Rank.ONE_PAIR, determine_hand_strength(hand))

    def test_high_card_true(self):
        hand = 'ABCDE'
        self.assertEqual(Rank.HIGH_CARD, determine_hand_strength(hand))

    def test_high_card_false(self):
        hand = 'AABCD'
        self.assertNotEqual(Rank.HIGH_CARD, determine_hand_strength(hand))
