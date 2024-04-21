
Certainly! Here's a basic example of a Discord bot script for playing music in Python using the discord.py library:

python
Copy code
import discord
from discord.ext import commands

# Import the necessary classes from the discord.py library
from discord import FFmpegPCMAudio
from discord.ext.commands import Bot

# Initialize the bot with a custom prefix
bot = Bot(command_prefix='!')

# Command to join a voice channel
@bot.command()
async def join(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        await ctx.send("You are not in a voice channel.")
        return

    channel = ctx.author.voice.channel
    if ctx.voice_client is not None:
        await ctx.voice_client.move_to(channel)
    else:
        await channel.connect()

    await ctx.send(f"Joined {channel}")

# Command to play music
@bot.command()
async def play(ctx, url: str):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        await ctx.send("You are not in a voice channel.")
        return

    channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await channel.connect()

    voice_client = ctx.voice_client

    try:
        # Attempt to play the audio stream from the provided URL
        voice_client.play(FFmpegPCMAudio(url))
        await ctx.send(f"Playing {url}")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

# Command to leave a voice channel
@bot.command()
async def leave(ctx):
    if ctx.voice_client is not None:
        await ctx.voice_client.disconnect()
        await ctx.send("Left voice channel.")
    else:
        await ctx.send("I am not connected to a voice channel.")

# Replace 'TOKEN' with your Discord bot token
bot.run('TOKEN')

# BY MAKIO 