import random
import re
import time
from collections import Counter

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

            # Check if the category affects sum
            if(str(category) == "Ones" or "Twos" or "Threes" or "Fours" or "Fives" or "Sixes"):

                self.__scores["Sum"] += int(value)

                # Check for bonus
                if(self.__scores["Sum"] >= 63):

                    self.update_score("Bonus", 50)
        
        return 0

    # Returns a specified category's score
    def check_category_score(self, category):

        return self.__scores[category]

def throw_dice(dices, throwing = ['1','2','3','4','5']):

    # "Throw" dice
    for dice in throwing:
        
        dices[dice] = random.randint(1,6)

    # Print the values and use sleep to increase tension
    print()
    print("1st dice: " + str(dices["1"]))
    time.sleep(0.5)
    print("2nd dice: " + str(dices["2"]))
    time.sleep(0.5)
    print("3rd dice: " + str(dices["3"]))
    time.sleep(0.5)
    print("4th dice: " + str(dices["4"]))
    time.sleep(0.5)
    print("5th dice: " + str(dices["5"]))
    print()
    time.sleep(0.5)
    
    return dices

# Function for choosing category
def choose_category(player_in_turn, dices):

    valid_input = False

    while(valid_input == False):

        categories = {"1" : "Ones",
                      "2" : "Twos",
                      "3" : "Threes",
                      "4" : "Fours",
                      "5" : "Fives",
                      "6" : "Sixes",
                      "7" : "One Pair",
                      "8" : "Two Pairs",
                      "9" : "Three of a Kind",
                      "10" : "Four of a Kind",
                      "11" : "Full House",
                      "12" : "Small Straight",
                      "13" : "Large Straight",
                      "14" : "Yatzy",
                      "15" : "Chance"}

        # Print categories
        print("{:<30}{:>30} ".format("1 : Ones", "_" * 14))
        print("{:<30}{:>30}".format("2 : Twos", "|   You got   |"))
        print("{:<30}{:>30}".format("3 : Threes", "| 1st dice: " + str(dices["1"]) + " |"))
        print("{:<30}{:>30}".format("4 : Fours","| 2nd dice: " + str(dices["2"]) + " |"))
        print("{:<30}{:>30}".format("5 : Fives", "| 3rd dice: " + str(dices["3"]) + " |"))
        print("{:<30}{:>30}".format("6 : Sixes", "| 4th dice: " + str(dices["4"]) + " |"))
        print("{:<30}{:>30}".format("7 : One Pair","| 5th dice: " + str(dices["5"]) + " |"))
        print("{:<30}{:>30} ".format("8 : Two Pairs", "-" * 14))
        print("9 : Three of a Kind")
        print("10 : Four of a Kind")
        print("11 : Full House")
        print("12 : Small Straight")
        print("13 : Large Straight")
        print("14 : Yatzy")
        print("15 : Chance")

        

        chosen_category = input("Press the number for which category you want to choose: ")

        # Check if the category is valid
        if(chosen_category in categories):

            category = categories[chosen_category]
            
            # Check if the player has chosen this category before
            if(player_in_turn.check_category_score(category) == 0):

                valid_input = True

                if(int(chosen_category) > 6):

                    print("Which number do you choose for {}?".format(category))
                    print("For straights you can leave this empty")
                    print("For Full House give the number that appears 3 times")
                    number = input("If the number doesn't matter press Enter: ")
                    value = category_score(dices, chosen_category, number)

                else:
                    value = sum_of_dices(dices, chosen_category)
                    
                player_in_turn.update_score(category, value)
                return 0
            
            else:

                print("Invalid category")

# Check input for invalid chars
def input_handler1(input_string):

    allowed_chars = [" ", "1", "2", "3", "4", "5"]

    for char in input_string:

        if(char not in allowed_chars):

            return False


    return True

# Handle input string and return a list
def string_handler(input_string):

    throw_list = []

    for char in input_string:

        if(char == "1" or "2" or "3" or "4" or "5"):

            throw_list.append(char)

    return throw_list

def sum_of_dices(dices, numbers='0'):

    sum = 0

    for key in dices:

        if(str(dices[key]) == numbers):

            sum += dices[key]

    return sum

def category_score(dices, category, number):

    count1 = 0
    count2 = 0
    number_to_check = 0
    value = 0

    # One pair
    if category == "7":

        for key in dices:

            if dices[key] == number:

                count1 += 1

        if count1 < 2:

            return 0
        
        else:

            return number * 2
        
    # Two Pairs
    elif category == "8":

        dice_counts = Counter(dices.values())

        pairs = [key for key, count in dice_counts.items() if count == 2]

        if len(pairs) == 2:

            sum_of_pairs = sum(int(key) for key in pairs) * 2
            return sum_of_pairs
        
        else:

            return 0


    # Three of a Kind
    elif category == "9":

        for key in dices:

            if dices[key] == number:

                count1 += 1

        if count1 >= 3:

            return number * 3
        
        else:

            return 0

    # Four of a Kind
    elif category == "10":

        for key in dices:

            if dices[key] == number:

                count1 += 1

        if count1 >= 4:

            return number * 4
        
        else:

            return 0

    # Full House
    elif category == "11":

        for key in dices:

            if dices[key] == number:

                count1 += 1

            else:
                
                if number_to_check == 0:

                    number_to_check = dices[key]
                    count2 += 1
                
                else:
                    
                    if(number_to_check == number):

                        count2 += 1

                    else:

                        return 0
        
        if count1 == 3 and count2 == 2:

            value = (number * 3) + (number_to_check * 2)

            return value

    # Small Straight
    elif category == "12":

        for i in range(1,7):

            count1 = 0

            for key in dices:

                if dices[key] == i:
                    
                    # 6 is not a part of Small Straight
                    if dices[key] == 6:

                        return 0
                    
                    count1 += 1

            if count1 > 1:

                return 0
            
        return 15
            

    # Large Straight
    elif category == "13":

        for i in range(1,7):

            count1 = 0

            for key in dices:

                if dices[key] == i:
                    
                    # 1 is not a part of Large Straight
                    if dices[key] == 1:

                        return 0
                    
                    count1 += 1

            if count1 > 1:

                return 0
            
        return 20

    # Yatzy
    elif category == "14":

        for key in dices:

            if number_to_check == 0:

                number_to_check = dices[key]

            if dices[key] != number_to_check:

                return 0

        return 50

    # Chance
    elif category == "15":

        value = 0

        for key in dices:

            value += dices[key]

        return value

# Core how the game works
def game(player1, player2):

    game_over = False
    turn = 0
    throw_counter = 0
    
    while(game_over == False):

        throw_counter = 0
        valid_input = False

        scoreboard(player1, player2)

        # Check for who's turn
        player_in_turn = player1 if turn == 0 else player2

        print("It's {}'s turn!".format(player_in_turn.get_name()))

        dices = {"1" : 0,
                 "2" : 0,
                 "3" : 0,
                 "4" : 0,
                 "5" : 0}

        while(throw_counter < 2):

            input("Press Enter to throw dice...")

            dices = throw_dice(dices)
            throw_counter = 1

            if(throw_counter == 1):

                while(valid_input == False):

                    print("Which dices do you want to throw again? (Use spaces between numbers)")
                    input_string = input("If you don't want to throw again press Enter... ")

                    # Player pressed Enter
                    if(input_string == ""):

                        valid_input = True
                        throw_counter = 2
                        choose_category(player_in_turn, dices)

                    # Player gave valid input
                    elif(input_handler1(input_string)):

                        valid_input = True
                        throw_dice(dices, string_handler(input_string))
                        choose_category(player_in_turn, dices)
                        throw_counter = 2

                    # Invalid input
                    else:
                        print("Invalid input")
                        input_string = ""

        turn = 1 if turn == 0 else 0


def game_over(player1, player2):

    for key in player1.get_scores:

        if(player2.get_scores[key] == "-" and key != "Bonus"):

            return False

    return True

# Printing scoreboard
def scoreboard(player1, player2):

    categories = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Sum", "Bonus",
                  "One Pair", "Two Pairs", "Three of a Kind", "Four of a Kind", "Full House",
                    "Small Straight","Large Straight", "Yatzy", "Chance", "Total"]
    

    print("_" * 69)
    print("| {:^66} |".format("SCOREBOARD"))
    print("|" + "-" * 68 + "|")
    print("| {:<20} | {:^20} | {:^20} |".format("Category", player1.get_name(), player2.get_name()))
    print("|" + "-" * 68 + "|")

    for category in categories:

        # Added so that 20 isn't replaced with 2- etc.
        #if (player1.check_category_score(category) == 0 and player2.check_category_score(category) == 0):

            #print("| {:<20} | {:^20} | {:^20} |".format(category, player1.get_scores()[category], player2.get_scores()[category]).replace("0", "-"))

        #else:

            #print("| {:<20} | {:^20} | {:^20} |".format(category, player1.get_scores()[category], player2.get_scores()[category]))

        print("| {:<20} | {:^20} | {:^20} |".format(category, player1.get_scores()[category], player2.get_scores()[category]).replace("0", "-"))

        if(category == "Sixes" or category == "Chance" or category == "Bonus"):

            print("|" + "-" * 68 + "|")

    print("|" + "_" * 68 + "|")

def main():

    player1_name = input("Player1 name: ")
    player2_name = input("Player2 name: ")

    player1 = Player(player1_name)
    player2 = Player(player2_name)

    game(player1, player2)

if __name__ == "__main__":
    main()
