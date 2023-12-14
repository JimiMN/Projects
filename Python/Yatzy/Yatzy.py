"""
This file consists of the core game for Yatzy

"""
import random
import re
import time
import Category_scores
from Player import Player


def throw_dice(dices, throwing = ['1','2','3','4','5']):

    # "Throw" dice
    for dice in throwing:
        
        dices[dice] = random.randint(1,6)

    # Print the values and use sleep to increase tension
    print()
    print("1st dice: " + str(dices["1"]))
    time.sleep(0.25)
    print("2nd dice: " + str(dices["2"]))
    time.sleep(0.25)
    print("3rd dice: " + str(dices["3"]))
    time.sleep(0.25)
    print("4th dice: " + str(dices["4"]))
    time.sleep(0.25)
    print("5th dice: " + str(dices["5"]))
    print()
    time.sleep(0.25)
    
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
                value = category_handler(dices, chosen_category)
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



def category_handler(dices, category):

    # Ones
    if category == "1":

        return Category_scores.number_scores(dices, 1)
    
    # Twos
    elif category == "2":

        return Category_scores.number_scores(dices, 2)
    
    # Threes
    elif category == "3":

        return Category_scores.number_scores(dices, 3)
    
    # Fours
    elif category == "4":

        return Category_scores.number_scores(dices, 4)
    
    # Fives
    elif category == "5":

        return Category_scores.number_scores(dices, 5)
    
    # Sixes
    elif category == "6":

        return Category_scores.number_scores(dices, 6)

    # One pair
    if category == "7":

        return Category_scores.one_pair(dices)
        
    # Two Pairs
    elif category == "8":

        return Category_scores.two_pairs(dices)


    # Three of a Kind
    elif category == "9":

        return Category_scores.three_of_a_kind(dices)

    # Four of a Kind
    elif category == "10":

        return Category_scores.four_of_a_kind(dices)

    # Full House
    elif category == "11":

        return Category_scores.full_house(dices)

    # Small Straight
    elif category == "12":

        return Category_scores.small_straight(dices)
            

    # Large Straight
    elif category == "13":

        return Category_scores.large_straight(dices)

    # Yatzy
    elif category == "14":

        return Category_scores.yatzy(dices)

    # Chance
    elif category == "15":

        return Category_scores.chance(dices)

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
        player_in_turn.update_sum()

def game_over(player1, player2):

    for key in player1.get_scores:

        if(player2.get_scores[key] == 0 and key != "Bonus"):

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

        print("| {:<20} | {:^20} | {:^20} |".format(category, player1.get_scores()[category], player2.get_scores()[category]))

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
