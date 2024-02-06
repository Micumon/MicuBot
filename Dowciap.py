import os
import discord
from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv("DISCORD_GUILD")
me = "micu_ta"
eltin = "eltin."

intents = discord.Intents.all()



client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    guild = client.guilds
    print(guild)


@client.event
async def on_message(message: discord.Message):
    print(f"{message.author.display_name}({message.guild},{message.channel}):")
    print(f"\t'{message.content}'")
    if message.author == client.user or message.author.name == me or message.author.name == eltin:
        return
    await message.add_reaction("\U0001F984")
    await message.add_reaction("\U0001F916")


client.run(TOKEN)
