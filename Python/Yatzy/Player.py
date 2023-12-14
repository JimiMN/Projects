"""
This file has the class "Player" and it's methods etc.

"""


# Class for players
class Player:

    #Constructor
    def __init__(self, name):
    
        self.__name = name
        self.__scores = {
            "Ones"            : 0,
            "Twos"            : 0,
            "Threes"          : 0,
            "Fours"           : 0,
            "Fives"           : 0,
            "Sixes"           : 0,
            "Sum"             : 0,
            "Bonus"           : 0,
            "One Pair"        : 0,
            "Two Pairs"       : 0,
            "Three of a Kind" : 0,
            "Four of a Kind"  : 0,
            "Full House"      : 0,
            "Small Straight"  : 0,
            "Large Straight"  : 0,
            "Yatzy"           : 0,
            "Chance"          : 0,
            "Total"           : 0,
        }

    # Get method for scores 
    def get_scores(self):

        return self.__scores

    # Get method for player's name
    def get_name(self):

        return self.__name

    # Method for updating a particular score
    def update_score(self, category, value):
        
        #Check if the value is 0
        if(value == 0):

            value = 'X'
            self.__scores[str(category)] = value

        else:

            # Update the category and total for the player
            self.__scores[str(category)] = value
            self.__scores["Total"] += int(value)

        # Check for bonus
        if(self.__scores["Sum"] >= 63):

            self.__scores["Bonus"] = 50
        
        return 0

    # Returns a specified category's score
    def check_category_score(self, category):

        return self.__scores[category]
    
    def update_sum(self):

        sum = 0

        # Check that value isnt "X"
        if self.check_category_score("Ones") != "X":

            sum += self.check_category_score("Ones")

        if self.check_category_score("Twos") != "X":

            sum += self.check_category_score("Twos")

        if self.check_category_score("Threes") != "X":

            sum += self.check_category_score("Threes")

        if self.check_category_score("Fours") != "X":

            sum += self.check_category_score("Fours")

        if self.check_category_score("Fives") != "X":

            sum += self.check_category_score("Fives")

        if self.check_category_score("Sixes") != "X":

            sum += self.check_category_score("Sixes")

        self.__scores["Sum"] = sum

        return 0