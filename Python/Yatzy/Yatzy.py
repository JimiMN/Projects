# Class for players
class Player:

    #Constructor
    def __init__(self, name):
    
        self.__name = name
        self.__scores = {
            "ones"            : "-",
            "twos"            : "-",
            "threes"          : "-",
            "fours"           : "-",
            "fives"           : "-",
            "sixes"           : "-",
            "total1"          : "-",
            "bonus"           : "-",
            "three of a kind" : "-",
            "four of a kind"  : "-",
            "full house"      : "-",
            "small straight"  : "-",
            "large straight"  : "-",
            "yatzy"           : "-",
            "chance"          : "-",
            "total2"          : "-",
        }

    # Get function for everything on the scoreboard
    def get_ones(self):
        
        return self.__scores["ones"]

    def get_twos(self):

        return self.__scores["twos"]
    
    def get_threes(self):
    
        return self.__scores["threes"]

    def get_fours(self):

        return self.__scores["fours"]
    
    def get_fives(self):

        return self.__scores["fives"]
    
    def get_sixes(self):

        return self.__scores["sixes"]
    
    def get_total1(self):

        return self.__scores["total1"]
    
    def get_total(self):

        if (self.__scores["total1"] >= 63 ):

            return 50
        
        else:

            return 0

    def get_three_of_a_kind(self):
        
        return self.__scores["three of a kind"]
    
    def get_four_of_a_kind(self):

        return self.__scores["four of a kind"]
    
    def get_full_house(self):
        
        return self.__scores["full house"]

    def get_small_straight(self):

        return self.__scores["small straight"]

    def get_large_straight(self):

        return self.__scores["large straight"]
    
    def get_yatzy(self):

        return self.__scores["yatzy"]
    
    def get_chance(self):

        return self.__scores["chance"]
    
    def get_total2(self):

        sum = 0

        for key in self.__scores:

            if(self.__scores[key] != "-"):

                sum = sum + self.__scores[key]

        self.__scores["total2"] = sum

        return self.__scores["total2"]
            

# Make the initial scoreboard
def initialize_scoreboard():

    print("--------------SCOREBOARD--------------")
    print("--------------------------------------")
    print("--------------Player1-|-Player2-------")
    print("Ones: \t\thalo \t halo")
    print("Twos: \t\thalo \t halo")
    print("Threes: \thalo \t halo")
    print("Fours: \t\thalo \t halo")
    print("Fives: \t\thalo \t halo")
    print("Sixes: \t\thalo \t halo")
    print("Total: \t\thalo \t halo")
    print("Bonus: \t\thalo \t halo")
    print("Three of a Kind: \t\thalo \t halo")
    print("Four of a Kind: \t\thalo \t halo")
    print("Full House: \t\thalo \t halo")
    print("Small Straight: \t\thalo \t halo")
    print("Large Straight: \t\thalo \t halo")
    print("Yatzy: \t\thalo \t halo")
    print("Chance: \t\thalo \t halo")
    print("Total: \t\thalo \t halo")

def main():

    player1_name = input("Player1 name: ")
    player2_name = input("Player2 name: ")

    Player(player1_name)
    Player(player2_name)

    initialize_scoreboard()

if __name__ == "__main__":
    main()
