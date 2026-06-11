'''
TaekwonBot Source Code
'''

import discord
from discord.ext import commands
from discord import app_commands
from bot_commands import bot_commands
import misc_functions as mf

from random import choice as randchoice
from config import TOKEN, GUILD
from datetime import datetime

# Create an intents object
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.reactions = True
intents.members = True

# Initialize the bot with the specified intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: When the bot is ready and connected to Discord
@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f'{bot.user} has connected to Discord!')
    print(f'Guild: {guild.name}')

    # Register the slash commands
    guild_id = discord.Object(id=guild.id)
    bot.tree.copy_global_to(guild=guild_id)
    await bot.tree.sync(guild=guild_id)

# Event: When a new member joins the server
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to UCTKD! We\'re excited to have you. ' +
        f'Please select the appropriate role in the Verification channel, ' +
        f'Just Interested or Active Member, to receive access to the other ' +
        f'relevant channels. Thank you and pil sung!'
    )

# Event: When a message is sent
@bot.event
async def on_message(message):
    # To prevent the bot from responding to itself (infinite loop)
    if message.author == bot.user:
        return
    
    # To prevent the bot from responding to other bots
    if message.author.bot:
        return
    
    # for the bot to see if it's a command instead of a normal message
    await bot.process_commands(message)

    # If "pil sung" is in the message content, react with the specified emoji
    if 'pil sung' in message.content.lower():
        emoji = bot_commands["pil_sung_id"]
        await message.add_reaction(emoji)
    
    # If "happy birthday" is in the message, react with a bday related emoji
    if "happy birthday" in message.content.lower() or "happy bday" in message.content.lower():
        bday_emojis = ["🎂", "🥳", "🎉"]
        emoji = randchoice(bday_emojis)
        await message.add_reaction(emoji)
    
    # If a message is in sniping channel and has an image, add it to the "database"
    if message.channel.id == bot_commands["sniping_id"] and mf.has_image(message):
        # prune old entries if necessary
        mf.prune_counts(bot_commands["sniping_dict"])
        # Add count to current day
        bot_commands["sniping_dict"][datetime.now().date()] += 1
        print(bot_commands["sniping_dict"])
    else:
        print("no images")

#####################################################################
#
# Slash commands
#
#####################################################################
# /dues
@bot.tree.command(name='dues',
             description='Explains the club\'s structure for yearly dues.')
async def dues(interaction: discord.Interaction):
    dues_fancy = bot_commands['dues']
    await interaction.response.send_message(dues_fancy)

# /funfact
@bot.tree.command(name='funfact',
             description='Sends a random TKD fun fact.')
async def funfact(interaction: discord.Interaction):
    fact = randchoice(bot_commands['funfact'])
    await interaction.response.send_message(fact)

# /flipcoin
@bot.tree.command(name="flipcoin", description="Flips a coin.")
async def flipcoin(interaction: discord.Interaction):
    flip = randchoice(['Heads', 'Tails'])
    await interaction.response.send_message(flip)

# /workout
# need js to put parameters in a slash command
@bot.tree.command(name="workout", description="Generates a random 10-exercise workout.")
async def workout(interaction: discord.Interaction):
    await interaction.response.send_message(mf.generate_warmup(10))

#####################################################################
#
# GIF Commands: UCTKD-specific gifs that users can send to each other
#
#####################################################################
# wasted
@bot.tree.command(name="wasted", description="GTA \"Wasted\" style GIF")
async def wasted(interaction: discord.Interaction):
    await interaction.response.send_message(file=discord.File("gifs/wasted.gif"))

# Sha dancing
@bot.tree.command(name="sha_dance", description="GIF of Master Shá vibing.")
async def sha_dance(interaction: discord.Interaction):
    await interaction.response.send_message(file=discord.File("gifs/shadance.gif"))

# hotel motel holiday inn gif
@bot.tree.command(name="pitbull", description="HOTEL MOTEL HOLIDAY INNNNN")
async def pitbull(interaction: discord.Interaction):
    await interaction.response.send_message(file=discord.File("gifs/hotelmotelholidayinn.gif"))

# Run the bot with the token
bot.run(TOKEN)
