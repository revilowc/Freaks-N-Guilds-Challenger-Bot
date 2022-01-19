import discord
import os
import time
from discord.ext import commands

#Add bot token here
TOKEN = ""

intents = discord.Intents.all()
client = commands.Bot(
    command_prefix=commands.when_mentioned_or('!'),
    activity=discord.Game(name="challenges by Freaks N' Guilds"),
    intents=intents,
    help_command=None,
    case_insensitive=True)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
    enlistedchannel = client.get_channel(925268802718027796)
    godrole = message.guild.get_role(896504910152089653)

    if message.content[:2].lower() == "0x" and message.channel == enlistedchannel:
        with open("walletaddresses.txt", "a") as f:
            f.write(f"\n{message.author.name}#{message.author.discriminator}:{message.content},")

        await message.delete()
        await message.channel.send(f"Got it! {message.author.mention}'s wallet address has been stored as `'{message.content}'`!")

    elif message.channel == enlistedchannel and message.content[:2].lower() != "0x" and message.author != client.user and godrole not in message.author.roles:
        await message.channel.send("Please refrain from talking in this channel. Only wallet addresses should be sent here!")

@commands.is_owner()
@client.command(pass_context=True)
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')
	await ctx.reply(embed=discord.Embed(
	    description=f"**Loaded '{extension}' cog**", color=0x000ff))
	time.sleep(1)
	await ctx.channel.purge(limit=2)

@commands.is_owner()
@client.command(pass_context=True)
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')

	await ctx.reply(embed=discord.Embed(
	    description=f"**Unloaded '{extension}' cog**", color=0x000ff))
	time.sleep(1)
	await ctx.channel.purge(limit=2)

@commands.is_owner()
@client.command(pass_context=True)
async def reload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	client.load_extension(f'cogs.{extension}')

	await ctx.reply(embed=discord.Embed(
	    description=f"**Reloaded '{extension}' cog**", color=0x000ff))
	time.sleep(1)
	await ctx.channel.purge(limit=2)

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
