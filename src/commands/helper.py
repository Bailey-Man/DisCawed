# store useful functions for commands
import regex as re
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




def convert_steamid3_to_steamid64(steamid3):
    # remove the [U:1: prefix and the ] suffix if they exist
    if type(steamid3) == str:
        steamid3 = steamid3[5:-1]

    

    
    
    steamid64 = int(steamid3) + 76561197960265728  # Add the base SteamID64 value
    return str(steamid64)