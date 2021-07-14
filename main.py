import discord
from Packages import Utils
from database import db


yfi = Utils.Finance()


## Our bot 
token = open("token.txt","r").read()
client = discord.Client()
@client.event
async def on_ready():
##Things to do 
    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )        
        
    #general_channel = client.get_channel(855657973438611467)
    #await general_channel.send('Hello, World!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('quote!'):
        t = message.content.split(":")[1]
        resp = yfi.get_ticker(ticker=t)
        await message.channel.send(resp)
      

## Run the client 
client.run(token)
