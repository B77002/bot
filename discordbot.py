import requests
import discord
from discord.ext import commands
from discord import Activity, ActivityType
from discord.ext import tasks



intents = discord.Intents.default()
intents.members = True  # Subscribe to the privileged members intent.
client = commands.Bot (command_prefix = '!', case_insensitive=True, intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
    ip = '80.249.113.74:30120'
    r = requests.get("http://"+ip+"/players.json")
    r1 = r.json()

    await client.change_presence(activity=Activity(name=f"{len(r1)} Players", type=ActivityType.watching))
    status.start()
    print('ready')


@tasks.loop(seconds=20, reconnect=True)
async def status():
    ip = '80.249.113.74:30120'
    r = requests.get("http://"+ip+"/players.json")
    r1 = r.json()

    await client.change_presence(activity=Activity(name=f"{len(r1)} Players", type=ActivityType.watching))



client.run('NzY3MzQ1NDUzNzc1NTg1Mjgw.X4wkJA.D2Rjna843PVTUZ8BpPjyQ74Fmlw')


