import discord
from requests.models import Response
from Packages import Utils     
                                                        

yfi = Utils.Finance()
## Our bot 
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
    
    if message.content.lower().startswith('div!'):
        d = message.content.split(" ")[1]
        div = yfi.get_dividend(ticker=d)
        await message.channel.send(div)

    if message.content.lower().startswith('wl!'):
        user_list = yfi.get_userlist(message.author.name)
        userid = message.author.id
        ment = message.author.mention
        embedVar = discord.Embed(title=f'Watch List', description=f"Stocks {ment} likes!", color=0x00ff00)
        i = 1
        for t in user_list:
            embedVar.add_field(name=f'Stock{i}:', value=t, inline=False)
            i+=1
        embedVar.set_footer(text="Cheers!!")
        await message.channel.send(embed=embedVar)
      
    if message.content.lower().startswith('wla!'):
        t = message.content.split(":")[1]
        await message.channel.send(yfi.add_userlist_item(message.author.name, t))

    if message.content.lower().startswith('wld!'):
        t = message.content.split(":")[1]
        await message.channel.send(yfi.del_userlist_item(message.author.name, t))    
      

## Run the client 
client.run('ODU3Njg5OTQyNjkwODg5NzM4.YNTQAQ.E3s4n8zRuuV6vGw5CZppN5DcfyM')
