import os
import discord
from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv("DISCORD_GUILD")
me = "micu_ta"
eltin = "eltin."
dorian = "dorianwilczynski"

intents = discord.Intents.all()
client = discord.Client(intents=intents)

message_to_dorian: discord.Message


@client.event
async def on_typing(channel: discord.TextChannel, user: discord.Member, when):
    global message_to_dorian
    async for message in channel.history(limit=1):
        if message.author == client.user:
            return
    message = ("W swojej wiadomości napisz w dowolnym miejscu:\n "
               "- /dr - jeżeli jesteś Drenorem\n"
               "- /el - jeżeli jesteś Eltinem. ")
    if user.name == dorian:
        message_to_dorian = await channel.send(message)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    guild = client.guilds
    print(guild)


@client.event
async def on_message(message: discord.Message):
    global message_to_dorian
    print(f"{message.author.display_name}({message.guild},{message.channel}):")
    print(f"\t'{message.content}'")
    if message.author == client.user:
        return
    drenor_message = "Poniższą wiadomość napisał:\nDrenor:"
    eltin_message = "Poniższą wiadomość napisał:\nEltin:"
    no_body = "<@1148275018590060628> nie podał kim jest!"
    if message.author.name == dorian:
        if message.content.find("/dr") != -1:
            await message_to_dorian.edit(content=drenor_message)
        elif message.content.find("/el") != -1:
            await message_to_dorian.edit(content=eltin_message)
        else:
            await message_to_dorian.edit(content=no_body)
    # if message.author == client.user or message.author.name == me or message.author.name == eltin:
    #     return
    # await message.add_reaction("\U0001F984")
    # await message.add_reaction("\U0001F916")


client.run(TOKEN)
