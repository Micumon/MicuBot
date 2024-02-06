# bot.py
import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv("DISCORD_GUILD")

intents = discord.Intents.all()



bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name="hi", help="Wita się z użytkownikiem.")
async def hi_command(ctx: discord.ext.commands.Context):
    await ctx.send(file=discord.File("Assets/k8.jpg"))



@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


@bot.command(name="create_channel")
@commands.has_role("admin")
async def create_channel_command(ctx: discord.ext.commands.Context, channel_name="New_channel"):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)



bot.run(TOKEN)

# client = discord.Client(intents=intents)
# @client.event
# async def on_ready():
#     print(f'{client.user.name} has connected to Discord!')
#     guild = client.guilds
#     print(guild)
#
#
# @client.event
# async def on_message(message: discord.Message):
#     if message.author == client.user:
#         return
#     print(message.content)
#
#     if message.content == "Cześć":
#         await message.channel.send("Siema!")
#     elif message.content == 'raise-exception':
#         raise discord.DiscordException
#
#
# @client.event
# async def on_error(event, *args, **kwargs):
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise



# client.run(TOKEN)
