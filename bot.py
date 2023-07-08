import discord
from discord.ext import commands

from food_picker import pick_cuisine


TOKEN = 'MTEwODIzNDQ3NDMwODc3NjAwNg.GPLnns.4eyC7YhLkXs9i8YLc7H2NqbF8R5Rf3wRgC5bJg'

### Bot Setup Code
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
prefix = '/'
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print('Ready!')

@bot.command(name='food', description='Choose what food you want.')
async def food(ctx, *args):
    cuisine = args[0]
    picked_cuisine = pick_cuisine(cuisine)
    await ctx.send(f"{picked_cuisine}")

bot.run(TOKEN)

'mexican'
