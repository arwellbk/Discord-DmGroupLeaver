import discord
bot = discord.Client()


@bot.event
async def on_ready():
    print("Use .lv command to leave groups.")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        command = message.content.strip().split(' ')
        cmd = command[0]
        if cmd == ".lv":
            await message.delete()
            for c in bot.private_channels:
                if isinstance(c, discord.GroupChannel):
                    byp = []  # Enter the IDs of the groups to be bypassed
                    if not c.id in byp:
                        await c.leave()
            print("Success")
            await bot.close()
TOKEN = "your accounts token goes here"
bot.run(TOKEN, bot=False)

'''https://github.com/arwellbk'''
