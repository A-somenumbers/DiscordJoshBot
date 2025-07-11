import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"josh, {bot.user.name}")


@bot.event
async def on_member_join(member):
    await  member.send(f"Joshing {member.name}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)


@bot.command()
async def josh(ctx):
    embed = discord.Embed(title="josh", description="Josh")
    embed.set_image(url="https://static.wikia.nocookie.net/flobbies/images/9/9a/Front-Facing_Yoshi_Render.jpg/revision/latest?cb=20210705164554")
    await ctx.send(embed=embed)


@bot.command()
async def cheerleader(ctx):
    await ctx.send("https://open.spotify.com/track/779mhz1mAry946r91qzR1r?si=0fa524a97d8647d5")


@bot.command()
async def job(ctx):
    embed = discord.Embed(title="Get a Job", description="u bum")
    embed.set_image(url="https://eforms.com/images/2018/03/Employment-Job-Application.png")
    await ctx.send(embed=embed)
    await ctx.send("https://www.indeed.com/")
    await ctx.send("https://www.linkedin.com/")


@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="New Poll", description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("💀")
    await poll_message.add_reaction("😭")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
