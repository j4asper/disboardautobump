import discord, asyncio
from discord.ext import commands
from random import randint

# Put your User Token between the quotations marks below
USER_TOKEN = "USER TOKEN HERE"

# Server ID of the server you want to be bumped.
SERVER_ID = "SERVER ID HERE"

# Put the channel ID, for the channel you are going to autobump from (The channel you would use to run !d bump)
CHANNEL = "CHANNEL ID HERE"







#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

bot = commands.Bot(command_prefix=None, selfbot=True)
bot.remove_command('help')
@bot.event
async def on_ready():
    print("+----------------------+")
    print("| Disboard Auto Bumper |")
    print("|          By          |")
    print("|        Jasper        |")
    print("|  Github.com/j4asper  |")
    print("+----------------------+")
    print("Auto bumping is against Disboard.org's ToS, and can get you and your server banned from the site!")
    print()
    channel = bot.get_channel(int(CHANNEL))
    if channel is None:
        print("INVALID CHANNEL ID!")
        print("INVALID CHANNEL ID!")
        print("INVALID CHANNEL ID!")
        print("Change the channel ID to a valid one!")
        await bot.close()
        input("Press enter to close this window.")

@bot.event
async def on_message(message):
    if message.author.id == 302050872383242240 and message.guild.id == int(SERVER_ID) and ("Check it on DISBOARD:" in message.embeds[0].description or "Check it on DISBOARD:" in message.content):
        # Adding a little buffer
        random = randint(0,500)

        # Two hour timer plus buffer
        await asyncio.sleep(7200+random)
        channel = bot.get_channel(int(CHANNEL))
        if channel is not None:
            # Trigger typing to look more legit
            async with channel.trigger_typing():
                await asyncio.sleep(2)
                await channel.send("!d bump")
        else:
            print("INVALID CHANNEL ID!")
            print("INVALID CHANNEL ID!")
            print("INVALID CHANNEL ID!")
            print("Change the channel ID to a valid one!")
            await bot.close()
            input()
    else:
        return

bot.run(USER_TOKEN, bot=False)