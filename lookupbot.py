import os
import discord 
from discord.ext import commands
import sys 
import requests
from dotenv import load_dotenv
# if /src not in path, add it
if sys.path.count('src') == 0:
    sys.path.append('src') # does this work correct??
else:
    print('src already in path')

from src.commands import helper

# init
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD') # is this not needed?
APIKEY = os.getenv('STEAM_API_KEY')


myintents = discord.Intents.default()
myintents.members = True
myintents.message_content = True

bot = commands.Bot(command_prefix='/', intents=myintents) 

### EVENTS ###
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('you do not have the correct role for this command')


### COMMANDS ###
@bot.command(name='lookup', help='lookup a user\'s steamid and return their username and avatar')
async def lookup_steam_user(ctx, *args):
    ## TODO ##
    # check that user making request has admin role
    # if not helper.check_role(ctx, 'admin'):
    #     await ctx.send('you do not have the correct role for this command')
    #     return None

    # names might have spaces in them, so join them back together
    name_id = ' '.join(args)
    
    print('name_id', name_id)
    # filter name_id for steamid3
    steamid3 = helper.extract_number(name_id)
    print('steamid3', steamid3)
    # convert steamid3 to steamid64
    steamid64 = helper.convert_steamid3_to_steamid64(steamid3)
    print('steamid64', steamid64)
    # Make a request to the Steam API to get user information
    response = requests.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={APIKEY}&steamids={steamid64}")

    ## does this work ???????
    if response.status_code == 200:
        data = response.json()
        print('data', data)
        # query json for username and avatar
        if 'response' in data and 'players' in data['response']:
            players = data['response']['players']
            if len(players) > 0:
                player = players[0]
                avatar = player.get('avatar', '')
                username = player.get('personaname', '')
                await ctx.send(f'username: {username}, avatar: {avatar}')



    else:
        print('error: ', response.status_code)
        await ctx.send('error: ', response.status_code)



bot.run(TOKEN)
