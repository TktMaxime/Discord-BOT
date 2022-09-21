from http import server
from discord.ext import commands
import discord
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
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


@bot.event
async def on_message(message):
    if message.content == "Salut tout le monde":
        await message.channel.send("Salut tout seul" + message.author.mention, reference=message)
    await bot.process_commands(message)


token = "MTAyMjE5MjU0MzQ0NzkwODM1NA.GtZk-t.EIq3eNhxQqFKGmn_EH99xrwAqq4QH7zkRp4GgA"
bot.run(token)  # Starts the bot
