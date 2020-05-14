import discord
from discord.ext import commands


#client = discord.Client()
bot = commands.Bot(command_prefix='$')

channel_set = False
misc_channel = 0
#misc_channel = 564671943106887695
misc_bot = 0
#misc_bot = 235088799074484224

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name = 'zhao')
async def _zhao(ctx, arg: int):
    global misc_channel
    misc_channel = arg
    channel_set = True
    print("Music Channel set to ： ", misc_channel)
    await ctx.send("Music channel set up complete, channel id: " + str(arg))


@bot.command(name = 'lis')
async def _lis(ctx, arg: int):
    global misc_bot
    misc_bot = arg
    print("Music bot set to: ", misc_bot)
    await ctx.send("music bot set as: " + str(arg))

@bot.event
async def on_message(msg):
    #print("inside",misc_channel,type(misc_channel))
    ch = bot.get_channel(misc_channel)
    if msg.channel.id != misc_channel and msg.content.startswith("!"):
        mover = msg
        #print(msg)
        #print("-----")
        #print(misc_bot, misc_channel)
        await msg.delete()
        await ch.send(msg.author.mention + " ***All music commands needs to be send in this channel***")
        await ch.send(msg.content)
    if msg.channel.id != misc_channel and msg.author.id == misc_bot:
        #print(msg.content)
        await msg.delete()
        #print(msg.embeds)
        if msg.embeds != []:
            await ch.send(content = msg.content, embed = msg.embeds[0])
        else:
            await ch.send(msg.content)
    await bot.process_commands(msg)

bot.run('YOUR TOKEN')