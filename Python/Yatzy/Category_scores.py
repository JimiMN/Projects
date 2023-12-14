"""
This file is for calculating scores in different situations

"""

from operator import countOf

def number_scores(dices, number):

    return countOf(dices.values(), number) * number

# Sum all of the dices
def sum_of_dices(dices):

    return dices['1'] + dices['2'] + dices['3'] + dices['4'] + dices['5']

# Check for pairs
def check_for_pair(dices):

    for i in range(1,7):

        if countOf(dices.values(), i) > 1:

            return True
    
    return False

# Calculate biggest pair
def one_pair(dices):

    biggest_pair = 0

    # No pairs
    if check_for_pair == False:

        return 0
    
    else:

        for i in range(1,7):

            if countOf(dices.values(), i) > 1 and i * 2 > biggest_pair:

                biggest_pair = i * 2
        

        return biggest_pair

# Calculate sum of two pairs
def two_pairs(dices):

    sum = 0
    found_pair = 0
    count_of_pairs = 0

    for i in range(1,7):

        # 4 or more of the same
        if countOf(dices.values(), i) >= 4:
            
            sum = i * 4
            return sum

        # Found pair
        elif countOf(dices.values(), i) > 1 and i != found_pair:

            sum += i * 2
            found_pair = i
            count_of_pairs += 1

    if count_of_pairs == 2:

        return sum
    
    else:

        return 0
    
# Find three of a kind and return sum
def three_of_a_kind(dices):

    for i in range(1,7):

        # If 3 of the same
        if countOf(dices.values(), i) >= 3:

            return i * 3
    
    return 0

# Find four of a kind and return sum
def four_of_a_kind(dices):

    for i in range(1,7):

        # If 4 of the same
        if countOf(dices.values(), i) >= 4:

            return i * 4
    
    return 0

# Full House
def full_house(dices):

    sorted_dices = sorted(dices.values())

    # Use set to find unique numbers and check if there 2 or 3 of one
    if len(set(sorted_dices)) == 2 and (sorted_dices.count(sorted_dices[0]) == 2 or 3):

        return sum(dices.values())
    
    else:
                
        return 0


# Check for small straight
def small_straight(dices):

    dice_values = sorted(dices.values())

    small_straight_list = [1,2,3,4,5]

    if(dice_values == small_straight_list):

        return 15
    
    else:

        return 0
    
# Check for large straight
def large_straight(dices):

    dice_values = sorted(dices.values())

    large_straight_list = [2,3,4,5,6]

    if(dice_values == large_straight_list):

        return 20
    
    else:

        return 0

# Yatzy aka 5 of a kind
def yatzy(dices):

    if countOf(dices.values(), dices['1']) == 5:

        return 50
    
    else:

        return 0

# Chance aka sum all dices
def chance(dices):

    return sum_of_dices(dices)