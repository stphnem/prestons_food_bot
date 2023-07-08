import discord
from discord.ext import commands

from food_picker import pick_cuisine


TOKEN = 'fill_token_here'

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
