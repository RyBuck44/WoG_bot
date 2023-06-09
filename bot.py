import random

import discord
from discord import app_commands
from discord.ext import commands
import os

secret_code = os.getenv('WoG_TOKEN')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


class db(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=1100490695309017168))
        self.synced = True
        print('Bot is Online')


bot = db()
tree = app_commands.CommandTree(bot)


@tree.command(name='help', description='provides information about bot function', guild=discord.Object(id=1100490695309017168))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message('PLease enter all the games you are willing to play.\n'
                                            'Use a comma (,) to separate them.\n'
                                            'I will take your list and make a decision for you.')


@tree.command(name='spin', description='prompts user to enter list of games, then will select and display one',
              guild=discord.Object(id=1100490695309017168))
async def self(interaction: discord.Interaction, games:str):
    all_games = games.split(',')
    the_game = random.choice(all_games)
    await interaction.response.send_message(f'Games you enterd : {games}\n'
                                            f'After some serious thought I think you should play {the_game}!\n'
                                            f'Have fun!')


def run_WoG_bot():
    bot.run(secret_code)


run_WoG_bot()