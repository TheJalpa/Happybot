import discord
from discord.ext import commands
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("!encourage"):
        await message.channel.send(random_line('inspire.txt'))
    if message.content.startswith("!kindwords"):
        await message.channel.send("{0.author.mention}".format(message) + random_line(" " + 'affirmation.txt'))
    if message.content.startswith("!sendkindwords"):
        user = message.mentions[0]
        uname = message.mentions[0].mention
        channel = await user.create_dm()
        botaction = random_line('botaction.txt')
        await channel.send("Hey there " + uname + ", it looks like " + "{0.author.mention}".format(message) + " wanted to send you something positive.\n" + botaction + "\n" + random_line('affirmation.txt'))
    if message.content.startswith("!fart"):
        user = message.mentions[0]
        channel = await user.create_dm()
        uname = message.mentions[0].mention
        content = "Well " + uname + " it looks like {0.author.mention}".format(message) + " has sent you.... a fart\nI'm very sorry about this, I didn't realize flatulence was in my code.\nFrankly, it stinks."
        await channel.send(content)

#Where the client id needs to be
client.run('')