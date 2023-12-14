"""
This file is for testing Yatzy.py, Category_scores.py and Player.py
"""

import Category_scores
import Yatzy
import Player
import unittest

class Test_category_scores(unittest.TestCase):

    def test_number_scores(self):
        
        dices1 = {"1" : 1,
                  "2" : 1,
                  "3" : 1,
                  "4" : 2,
                  "5" : 2}
        
        dices2 = {"1" : 4,
                  "2" : 4,
                  "3" : 5,
                  "4" : 5,
                  "5" : 6}

        dices3 = {"1" : 5,
                  "2" : 1,
                  "3" : 6,
                  "4" : 5,
                  "5" : 6}
        
        # Test Ones
        result = Yatzy.category_handler(dices1, '1')
        self.assertEqual(result, 3)

        # Test Twos
        result = Yatzy.category_handler(dices1, '2')
        self.assertEqual(result, 4)

        # Test Threes
        result = Yatzy.category_handler(dices1, '3')
        self.assertEqual(result, 0)

        # Test Fours
        result = Yatzy.category_handler(dices2, '4')
        self.assertEqual(result, 8)

        # Test Fives
        result = Yatzy.category_handler(dices2, '5')
        self.assertEqual(result, 10)

        # Bug with 2 fives giving 15 instead of 10
        result = Yatzy.category_handler(dices3, '5')
        self.assertEqual(result, 10)

        # Test Sixes
        result = Yatzy.category_handler(dices2, '6')
        self.assertEqual(result, 6)
    
    def test_pairs(self):
        
        dices1 = {"1" : 1,
                  "2" : 2,
                  "3" : 3,
                  "4" : 4,
                  "5" : 5}

        dices2 = {"1" : 5,
                  "2" : 5,
                  "3" : 4,
                  "4" : 4,
                  "5" : 4}

        dices3 = {"1" : 5,
                  "2" : 5,
                  "3" : 5,
                  "4" : 5,
                  "5" : 5}


        # One pair 1st 0, 2nd 5 * 2
        result = Yatzy.category_handler(dices1, '7')
        self.assertEqual(result, 0)

        result = Yatzy.category_handler(dices2, '7')
        self.assertEqual(result, 10)


        # Two pairs 1st 0, 2nd 18 and 3rd 20
        result = Yatzy.category_handler(dices1, '8')
        self.assertEqual(result, 0)

        result = Yatzy.category_handler(dices2, '8')
        self.assertEqual(result, 18)

        result = Yatzy.category_handler(dices3, '8')
        self.assertEqual(result, 20)

    # Test which should return correct amount and test which should fail for each
    def test_x_of_a_kind(self):

        dices1 = {"1" : 1,
                  "2" : 2,
                  "3" : 3,
                  "4" : 4,
                  "5" : 5}

        dices2 = {"1" : 6,
                  "2" : 6,
                  "3" : 6,
                  "4" : 6,
                  "5" : 6}

        # Test Three of a Kind
        result = Yatzy.category_handler(dices1, '9')
        self.assertEqual(result, 0)

        result = Yatzy.category_handler(dices2, '9')
        self.assertEqual(result, 18)


        # Test Four of a Kind
        result = Yatzy.category_handler(dices1, '10')
        self.assertEqual(result, 0)

        result = Yatzy.category_handler(dices2, '10')
        self.assertEqual(result, 24)


        # Test Yatzy
        result = Yatzy.category_handler(dices1, '14')
        self.assertEqual(result, 0)

        result = Yatzy.category_handler(dices2, '14')
        self.assertEqual(result, 50)

    def test_straights(self):

        dices1 = {"1" : 1,
                  "2" : 2,
                  "3" : 3,
                  "4" : 4,
                  "5" : 5}

        dices2 = {"1" : 2,
                  "2" : 3,
                  "3" : 4,
                  "4" : 5,
                  "5" : 6}
        
        # Test Small Straight
        result = Yatzy.category_handler(dices1, '12')
        self.assertEqual(result, 15)

        result = Yatzy.category_handler(dices2, '12')
        self.assertEqual(result, 0)

        # Test Large Straight
        result = Yatzy.category_handler(dices1, '13')
        self.assertEqual(result, 0)

        result = Yatzy.category_handler(dices2, '13')
        self.assertEqual(result, 20)


    def test_full_house_chance(self):

        dices1 = {"1" : 2,
                  "2" : 3,
                  "3" : 4,
                  "4" : 5,
                  "5" : 6}
        
        dices2 = {"1" : 2,
                  "2" : 6,
                  "3" : 2,
                  "4" : 6,
                  "5" : 6}
        

        # Test Full House
        result = Yatzy.category_handler(dices1, '11')
        self.assertEqual(result, 0)

        result = Yatzy.category_handler(dices2, '11')
        self.assertEqual(result, 22)

        # Test Chance
        result = Yatzy.category_handler(dices1, '15')
        self.assertEqual(result, 20)

        result = Yatzy.category_handler(dices2, '15')
        self.assertEqual(result, 22)       


if __name__ == '__main__':
    unittest.main()