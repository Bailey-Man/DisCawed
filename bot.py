# bot.py
import os
import random
import discord
from dotenv import load_dotenv
# get bot
from discord.ext import commands












load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD') # is this not needed?


myintents = discord.Intents.default()
# does this cover messages?
myintents.members = True
myintents.message_content = True



bot = commands.Bot(command_prefix='!', intents=myintents) 

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# message handler that catches if a string matches 'yee haw'
@bot.command(name='bird', help='yee caw')
async def bird(ctx):
    response = 'yee caw'
    await ctx.send(response)

# basic dice roll
@bot.command(name='roll', help='roll dice in number_of_dice, number_of_sides format!')
async def rolldice(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    # response is the sum of the dice
    sum_total = sum([int(i) for i in dice])


    response = ' + '.join(dice) + ' = ' + str(sum_total)

    await ctx.send(response)

###### TESTING #######
# query the chatGPT api for an image based on the user's message
@bot.command(name='image', help='query the chatGPT api for an image based on the user\'s message')
async def image(ctx, *args):
    # get the message
    message = ' '.join(args)
    # query the api
    response = 'https://chatgpt.com/api/v1/images?text=' + message
    await ctx.send(response)



##################

# run the bot
bot.run(TOKEN)




# # missing 'intents' parameter ?
# myintents = discord.Intents.default() # (messages=True, guilds=True, reactions=True, members=True)
# myintents.message_content = True
# myintents.members = True

# class CustomClient(discord.Client):#, intents=myintents):
#     async def on_ready(self):
#         print(f'{self.user} has connected to Discord!')
#         # self.intents = myintents        



# client = CustomClient()#intents=myintents)



# @client.event
# async def on_error(event, *args, **kwargs):
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise




# client.run(TOKEN)












# does ? this work ?? what is commands
# client = discord.Client(intents=myintents)
# print('client intents', client.intents)


# # When the bot is ready
# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')
#     guild = discord.utils.get(client.guilds, name=GUILD)

#     # Print the guild name and id
#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#     )

# # When a member joins the server for the first time, *DIAGNOSE THEM WITH DND RACE/CLASS*
# # @client.event
# # async def on_member_join(member):
# #     # if member in preset list; populate with that
# #     # else; diagnose from avatar and username

# #     await member.create_dm()
# #     await member.dm_channel.send(
# #         f'Hi {member.name}, welcome to the server!'
# #     )

# # # When a member leaves the server, post the rip bozo gif
# # @client.event
# # async def on_member_remove(member):
# #     await member.create_dm()
# #     await member.dm_channel.send(
# #         f'rip bozo'
# #     )



# # respond to user messages
# @client.event
# async def on_message(message):



#     print('do i even get this far?')
#     print(message.content)
#     print(message)
#     # if message sent by this bot; ignore
#     if message.author == client.user:
#         return
#     # if message is command !bird; respond with 'yee caw'
#     if message.content == '!bird':
#         response = 'yee caw'
#         await message.channel.send(response)
#     print('is it not bird?')



# # run the bot
# client.run(TOKEN)