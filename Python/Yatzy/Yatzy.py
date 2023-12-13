import random
import re

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
        
        # Update the category and total for the player
        self.__scores[str(category)] = value
        self.__scores["Total"] += value

        # Check if the category affects sum
        if(str(category) == "Ones" or "Twos" or "Threes" or "Fours" or "Fives" or "Sixes"):

            self.__scores["Sum"] += int(value)

            # Check for bonus
            if(self.__scores["Sum"] >= 63):

                self.update_score("Bonus", 50)

    def check_category_score(self, category):

        return self.__scores[category]

def throw_dice(throw_counter, throwing = [1,2,3,4,5]):


    if(throw_counter == 1):

        dices = {}

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    dice4 = random.randint(1,6)
    dice5 = random.randint(1,6)

    dices = {"1" : dice1,
             "2" : dice2,
             "3" : dice3,
             "4" : dice4,
             "5" : dice5,}
    
    return dices

# Function for choosing category
def choose_category(player_in_turn, dice_value):

    valid_input = False

    while(valid_input == False):

        categories = {"1" : "Ones",
                      "2" : "Twos",
                      "3" : "Threes",
                      "4" : "Fours",
                      "5" : "Fives",
                      "6" : "Sixes",
                      "7" : "Three of a Kind",
                      "8" : "Four of a Kind",
                      "9" : "Full House",
                      "10" : "Small Straight",
                      "11" : "Large Straight",
                      "12" : "Yatzy",
                      "13" : "Chance"}

        print("1 : Ones")
        print("2 : Twos")
        print("3 : Threes")
        print("4 : Fours")
        print("5 : Fives")
        print("6 : Sixes")
        print("7 : Three of a Kind")
        print("8 : Four of a Kind")
        print("9 : Full House")
        print("10 : Small Straight")
        print("11 : Large Straight")
        print("12 : Yatzy")
        print("13 : Chance")

        chosen_category = input("Press the number for which category you want to choose: ")

        if(chosen_category in categories):

            category = categories[chosen_category]
            
            if(player_in_turn.check_category_score(category) == 0):

                valid_input = True
                player_in_turn.update_score(category, dice_value)

            else:

                print("Invalid category")
    
    return 0

# Check input for invalid chars
def input_handler1(input_string):

    allowed_chars = ["1", "2", "3", "4", "5"]

    for char in input_string:

        if(char not in allowed_chars):

            return False


    return True

# Handle input string and return a list
def string_handler(input_string):

    throw_list = []

    for char in input_string:

        if(char == "1" or "2" or "3" or "4" or "5"):

            throw_list.append(int(char))

    return throw_list

def sum_of_dices(dices):

    sum = 0

    for key in dices:

        sum += dices[key]
    
    return sum

# Core how the game works
def game(player1, player2):

    game_over = False
    turn = 0
    throw_counter = 0
    valid_input = False
    
    while(game_over == False):

        throw_counter = 0

        scoreboard(player1, player2)

        if(turn == 0):

            player_in_turn = player1
        
        else:
            player_in_turn = player2

    

        while(throw_counter < 2):

            input("Press Enter to throw dice...")

            dices = throw_dice(throw_counter)
            throw_counter = 1

            print("1st dice: " + str(dices["1"]))
            print("2nd dice: " + str(dices["2"]))
            print("3rd dice: " + str(dices["3"]))
            print("4th dice: " + str(dices["4"]))
            print("5th dice: " + str(dices["5"]))

            if(throw_counter == 1):

                while(valid_input == False):

                    print("Which dices do you want to throw again? (Use spaces between numbers)")
                    input_string = input("If you don't want to throw again press Enter... ")

                    # Player pressed Enter
                    if(input_string == ""):

                        valid_input = True
                        throw_counter = 2
                        choose_category(player_in_turn, sum_of_dices(dices))

                    # Player gave valid input
                    elif(input_handler1(input_string)):

                        valid_input = True

                    # Invalid input
                    else:
                        print("Invalid input")
                        input_string = ""


        choose_category(player_in_turn, sum_of_dices(dices))
        throw_counter = 2

def game_over(player1, player2):

    for key in player1.get_scores:

        if(player2.get_scores[key] == "-" and key != "Bonus"):

            return False

    return True

# Printing scoreboard
def scoreboard(player1, player2):

    categories = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Sum", "Bonus",
                  "Three of a Kind", "Four of a Kind", "Full House", "Small Straight",
                  "Large Straight", "Yatzy", "Chance", "Total"]
    

    print("_" * 69)
    print("| {:^66} |".format("SCOREBOARD"))
    print("|" + "-" * 68 + "|")
    print("| {:<20} | {:^20} | {:^20} |".format("Category", player1.get_name(), player2.get_name()))
    print("|" + "-" * 68 + "|")

    for category in categories:

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
