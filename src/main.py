from http import server
from tkinter import dnd
from discord.ext import commands
import discord
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True,  # Commands aren't case-sensitive
    intents=intents  # Set up basic permissions
)


bot.author_id = 315167381284716544  # Change to your discord id


@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


@bot.command()
async def pong(ctx):
    await ctx.send('pong')


@bot.command()
async def name(ctx):
    await ctx.send(ctx.message.author)


@bot.command()
async def d6(ctx):
    await ctx.send(random.randrange(1, 7))


@bot.command()
async def admin(ctx, user: discord.Member):
    server = ctx.message.guild
    perms = discord.Permissions(8)
    role = discord.utils.get(ctx.guild.roles, name="Admin")
    if not role:
        await server.create_role(name='Admin', permissions=perms)
        role = discord.utils.get(ctx.guild.roles, name="Admin")
    await user.add_roles(role)


@bot.command()
async def ban(ctx, user: discord.Member):
    await user.ban(reason="aurevoir")


@bot.command()
async def count(ctx):
    server = ctx.message.guild
    online = []
    idle = []
    offline = []
    doNotDisturb = []

    for member in server.members:
        status = str(member.status)
        if status == "online":
            online.append(member)
        elif status == "dnd":
            doNotDisturb.append(member)
        elif status == "offline":
            offline.append(member)
        elif status == "idle":
            idle.append(member)
    await ctx.send("Those people are online")
    for elt in online:
        await ctx.send(elt)
    await ctx.send("Those people are idle")
    for elt in idle:
        await ctx.send(elt)
    await ctx.send("Those people are in do not disturb")
    for elt in doNotDisturb:
        await ctx.send(elt)
    await ctx.send("Those people are offline")
    for elt in offline:
        await ctx.send(elt)

    await ctx.send(f"{len(online)} are online, {len(idle)} are idle, {len(offline)} are offline and {len(doNotDisturb)} are in do not disturb")


@bot.command()
async def xkcd(ctx):
    await ctx.send("https://xkcd.com/")


@bot.command()
async def poll(ctx, arg):
    await ctx.send("@here" + arg)


@bot.event
async def on_message(message):
    if message.content == "Salut tout le monde":
        await message.channel.send("Salut tout seul" + message.author.mention, reference=message)
    await bot.process_commands(message)


token = "MTAyMjE5MjU0MzQ0NzkwODM1NA.GflTEP.2mTiwa8GRV0Cq15tGdetjym0hLnsqYvkC72tTA"
bot.run(token)  # Starts the bot
