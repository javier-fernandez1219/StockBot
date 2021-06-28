import discord

## Our bot 
client = discord.Client()

@client.event

async def on_ready():
##Things to do 
    general_channel = client.get_channel(855657973438611467)

    await general_channel.send('Hello, World!')

## Run the client 
client.run('ODU3Njg5OTQyNjkwODg5NzM4.YNTQAQ.E3s4n8zRuuV6vGw5CZppN5DcfyM')
