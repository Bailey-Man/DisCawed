import requests
import os 
# testing for steam api
import a2s
from dotenv import load_dotenv

load_dotenv()

# connectnumber = 27015 # what is this??
# server_address = (os.environ.get("SERVER_ADDRESS"), connectnumber) # what is this??

# a2s.info(server_address)

STEAM_API_KEY = os.environ.get("STEAM_API_KEY")

for i in os.environ:
    print(i)

# print('STEAM_API_KEY', STEAM_API_KEY)

def lookup(steamid):
    # format steamid into useable format
    print('steamid', steamid)

    # Make a request to the Steam API to get user information
    response = requests.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={STEAM_API_KEY}&steamids={steamid}")
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

# test_query = f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/{STEAM_API_KEY}/?steamids=76561198025098010'

# Endless Shrimp [U:1:1603354484]
test_steam_id = '[U:1:1603354484]'

test_id_num = '76561199563620212' # wtf

# response = requests.get(
#     f'{}'
# )



test = requests.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={STEAM_API_KEY}&steamids={test_id_num}")
# print('test', test)




# username_, avatar_ = lookup(
#     steamid=test_id_num
# )

# print('username', username_)






# def get_player_info(steamid):
#     # Perform the lookup using requests

#     # request from this url; https://steamid.uk/steamidapi/
#     response = requests.get(f"https://steamid.uk/steamidapi.php?api={STEAM_API_KEY}&steamids={steamid}")

#     # http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/

#     response = requests.get(f"https://api.example.com/users/{steamid}")
    
#     # Check if the request was successful
#     if response.status_code == 200:
#         data = response.json()
#         username = data["username"]
#         avatar = data["avatar"]
#     else:
#         # Handle the case when the lookup fails
#         username = "Unknown"
#         avatar = ""
    
#     return username, avatar
