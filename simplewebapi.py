import requests 
import os 
from dotenv import load_dotenv
load_dotenv() # what does this do??


class SteamWebApi:
    # get api key from .env file
    STEAM_API_KEY = os.environ.get("STEAM_API_KEY") # why doesnt this work?

    # temp_key = 
    base_url = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/" # is this the right url


STEAM_API_KEY = os.environ.get("STEAM_API_KEY")


# does this work?

convert_test_a = 1603354484
convert_test_b = 76561199563620212

print('convert_test_a', convert_steamid3_to_steamid64(convert_test_a))
print('convert_test_b', convert_test_b)



def lookup(steamid):
    # format steamid into useable format
    print('steamid', steamid)
    # TODO: make this loop through a potential list of steamids
    query_id = convert_steamid3_to_steamid64(steamid)

    
    # Make a request to the Steam API to get user information
    response = requests.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={STEAM_API_KEY}&steamids={query_id}")
    print('response', response)
    
    if response.status_code == 200:
        data = response.json()
        if 'response' in data and 'players' in data['response']:
            players = data['response']['players']
            if len(players) > 0:
                player = players[0]
                avatar = player.get('avatar', '') # this might be a png? or a link? see what happens...
                username = player.get('personaname', '')
                return username, avatar
    else: 
        print('error: ', response.status_code)
        return None, None
        



test_steam_id = '[U:1:1603354484]'

test_id_num = '76561199563620212' # wtf

steam_api_key = os.environ.get("STEAM_API_KEY")
# print('steam_api_key', steam_api_key)

# response = requests.get(
#     f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={steam_api_key}&steamids={test_id_num}'
# )

response = lookup(test_steam_id)

print('response', response)