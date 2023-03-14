import discord
from discord.ext import commands
from PingPongTool import PingPong
import asyncio

bot = commands.Bot(command_prefix='', intents=discord.Intents.all())

#ai---------------------------------------------------------------------------------------------------------------------

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------------')
    await bot.change_presence(activity=discord.Game("로동"), status=discord.Status.dnd)

URL = "https://builder.pingpong.us/api/builder/63f9f06ae4b04966c0b4f18b/integration/v0.2/custom/{sessionId}"
Authorization = "Basic a2V5OmY2MWRiMTFiYThjNmQ2YTNjODQ2MWRiZjI0YmY0NTAy"
Ping = PingPong(URL, Authorization)

@bot.command()
async def 노바야(ctx, 말):
    data = str(await Ping.Pong("Example", 말))
    await ctx.send(data[10:])

#토큰---------------------------------------------------------------------------------------------------------------------

bot.run("")