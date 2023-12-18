# store useful functions for commands
import regex as re
import datetime
import random 
# import re

def extract_number(string):
    # pattern = r'\[(\d+)\]'  # Matches a number between []
    # match a pattern which is a set of numbers between a : and a ]
    pattern = r':(\d+)\]'



    match = re.search(pattern, string)
    if match:
        return match.group(1)  # Returns the captured number
    else:
        print('no match found')
        return None  # No match found

def convert_unix_timestamp_to_date(timestamp):
    # convert unix timestamp to date
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')


### DND ###
def roll_dice(number_of_dice, number_of_sides):
    # basic dice roll
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    sum_total = sum([int(i) for i in dice])
    
    return sum_total

def roll_dnd_dice(adv_status, number_of_dice, number_of_sides):
    # check for advantage or disadvantage
    if adv_status == None:
        myroll = roll_dice(number_of_dice, number_of_sides)    
    else:
        # roll two sets of dice and take the higher value
        roll_a = roll_dice(number_of_dice, number_of_sides)
        roll_b = roll_dice(number_of_dice, number_of_sides)
        
        if adv_status == True:
            # return the higher value
            myroll = roll_a if roll_a > roll_b else roll_b
        elif adv_status == False:
            # return the lower value
            myroll = roll_a if roll_a < roll_b else roll_b
        else:
            print('adv_status not recognized', adv_status)
            myroll = roll_a

    return myroll

## stat rolls ##
def std_array():
    # standard array
    return [15, 14, 13, 12, 10, 8]

def point_buy():
    # point buy
    return 0 

def four_d6_drop_lowest():
    # 4d6 drop lowest
    return 0

def three_d6():
    # 3d6
    return 0

def two_d6_plus_6():
    # 2d6 + 6
    return 0

def one_d20():
    # 1d20
    return 0

def roll_stats(method='4d6 drop lowest'):
    '''
    methods:
    - standard array
    - point buy
    - 4d6 drop lowest
    - 3d6
    - 2d6 + 6
    - 1d20
    '''
    method_functions = {
        'standard array': std_array,
        'point buy': point_buy,
        '4d6 drop lowest': four_d6_drop_lowest,
        '3d6': three_d6,
        '2d6 + 6': two_d6_plus_6,
        '1d20': one_d20
    }
    return method_functions[method]() # test this


### STEAM ### 
def convert_steamid3_to_steamid64(steamid3):
    # remove the [U:1: prefix and the ] suffix if they exist
    steamid64 = int(steamid3) + 76561197960265728  # Add the base SteamID64 value
    return str(steamid64)