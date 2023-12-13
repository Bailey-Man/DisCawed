# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


# missing 'intents' parameter ?
myintents = discord.Intents(messages=True, guilds=True, reactions=True, members=True)
# intents.members = True

# does ? this work ?? what is commands
client = discord.Client(intents=myintents)
print('client intents', client.intents)


# When the bot is ready
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guild = discord.utils.get(client.guilds, name=GUILD)

    # Print the guild name and id
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

# When a member joins the server for the first time, *DIAGNOSE THEM WITH DND RACE/CLASS*
# @client.event
# async def on_member_join(member):
#     # if member in preset list; populate with that
#     # else; diagnose from avatar and username

#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to the server!'
#     )

# # When a member leaves the server, post the rip bozo gif
# @client.event
# async def on_member_remove(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'rip bozo'
#     )



# respond to user messages
@client.event
async def on_message(message):



    print('do i even get this far?')
    print(message.content)
    print(message)
    # if message sent by this bot; ignore
    if message.author == client.user:
        return
    # if message is command !bird; respond with 'yee caw'
    if message.content == '!bird':
        response = 'yee caw'
        await message.channel.send(response)



# run the bot
client.run(TOKEN)