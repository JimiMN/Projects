# Class for players
class Player:

    #Constructor
    def __init__(self, name):
    
        self.__name = name
        self.__scores = {
            "Ones"            : "-",
            "Twos"            : "-",
            "Threes"          : "-",
            "Fours"           : "-",
            "Fives"           : "-",
            "Sixes"           : "-",
            "Sum"             : "-",
            "Bonus"           : "-",
            "Three of a Kind" : "-",
            "Four of a Kind"  : "-",
            "Full House"      : "-",
            "Small Straight"  : "-",
            "Large Straight"  : "-",
            "Yatzy"           : "-",
            "Chance"          : "-",
            "Total"           : "-",
        }

    # Get method for scores 
    def get_scores(self):

        return self.__scores

    # Get player's name
    def get_name(self):

        return self.__name


# Printing scoreboard
def scoreboard(player1, player2):

    categories = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Sum", "Bonus",
                  "Three of a Kind", "Four of a Kind", "Full House", "Small Straight",
                  "Large Straight", "Yatzy", "Chance", "Total"]
    

    print("_" * 69)
    print("| {:^66} |".format("SCOREBOARD"))
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

    scoreboard(player1, player2)

if __name__ == "__main__":
    main()
