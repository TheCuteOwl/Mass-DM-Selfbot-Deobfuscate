import os 
os.system("pip install discord.py==1.7.3")
import discord 
from discord.ext import commands
os.system("pip install colorama")
from colorama import Fore 





token = input(f"{Fore.RED} Token :{Fore.RESET} ")
prefix = input(f"{Fore.RED} Enter Prefix :{Fore.RESET} ")

r = Fore.RESET 
intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, intents=intents, self_bot=True)
client.remove_command('help')


@client.event
async def on_ready():
	os.system("clear")
	print(f"{Fore.LIGHTCYAN_EX } LOGGED IN : {client.user.name}#{client.user.discriminator}{Fore.RESET}\n{Fore.LIGHTYELLOW_EX} Made By TheAxes{r}")
	await client.change_presence(activity=discord.Game(name="Axes Runs Cord"))



@client.command()
async def help(ctx):
	await ctx.message.delete()
	await ctx.send(f"""
	```
	
     >>> Made By TheAxes
	{prefix}help - Shows This Message
	{prefix}massdm <text>  -  Start Massdm
	{prefix}shutdown - Shutdown Selfbot | Turn Off
	     [Axe MassDm]
```
	""")

@client.command()
async def massdm(ctx, *, text):
	await ctx.reply("> Axe MassDm Started\n> Dming Members")
	for member in ctx.guild.members:
		try:
			await member.send(text)
			print(f"{Fore.GREEN}[+] {member.name}#{member.discriminator}{r}")
		except:
			print(f"{Fore.RED}Can't Message {member.name}#{member.discriminator} Reason = Dms Off{r}")

@client.command()
async def shutdown(ctx):
	await ctx.reply("> Axe MassDm | ShutDown Successfully")
	print("Turned Off")
	await client.close()

client.run(token, bot=False)
