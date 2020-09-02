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
    if message.content.startswith("!lottery"):
        user = message.author
        convuser = str(user)
        channel = await user.create_dm()
        with open("src/keysactive.txt", "r+") as f1, open("src/keysclaimed.txt", "r+") as f2, open("src/lotteryclaims.txt", "r+") as f3:
            f3lines = f3.readlines()
            f3.seek(0)
            badbool = False
            for line in f3lines:
                if line.startswith(convuser):
                    await channel.send("It looks like you've recently claimed a key from the lottery.  Please wait for an administrator to clear the lottery.")
                    badbool = True
                    break
            for line in f3.readlines():
                f3.seek(0)
                if badbool == True:
                    break
                if not line.startswith(convuser):
                    print("bruh")
                    f1lines = f1.readlines()
                    f2lines = f2.readlines()
                    randomline = random_line('src/keysactive.txt')
                    f1.seek(0)

                    for line in f1lines:
                        if not line.startswith(randomline):
                            f1.write(line)
                    for line in f2lines:
                        if line.startswith("\n"):
                            f2.write(randomline + "\n")
                            f3.seek(0)
                            data = f3.read(100)
                            if len(data) > 0 :
                                f3.write("\n")
                                f3.write(convuser)
                                f3.truncate()
                    f1.truncate()
                    f2.truncate()
                    

                    await channel.send("Wow, looks like someone got a steam key! " + randomline)
                    break

    if message.content.startswith("!encourage"):
        await message.channel.send(random_line('src/inspire.txt'))
    if message.content.startswith("!kindwords"):
        await message.channel.send("{0.author.mention.}".format(message) + random_line(" " + 'src/affirmation.txt'))
    if message.content.startswith("!sendkindwords"):
        user = user = message.mentions[0]
        print (user)
        uname = message.mentions[0].mention
        channel = await user.create_dm()
        botaction = random_line('src/botaction.txt')
        await channel.send("Hey there " + uname + ", it looks like " + "{0.author.mention}".format(message) + " wanted to send you something positive.\n" + botaction + "\n" + random_line('src/affirmation.txt'))
#" + "{0.author.mention}".format(message) + "



#Where the client id needs to be
#You can get this from your discord developer portal under your Bot page and add your token.
#You really only need to give it "bot" permissions, and that's it.
client.run('')