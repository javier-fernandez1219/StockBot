import discord
from discord.ext import commands
from requests.models import Response
from Packages import Utils     
from Packages import Configuration as cfg
                                                        

yfi = Utils.Finance()
## Our bot 
client = commands.Bot(command_prefix='#')

@client.event
async def on_ready():
##Things to do 
    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )        
        
@client.command(name='list', help='Use #list to view the stocks in your WL.')
async def list(ctx):
    user_list = yfi.get_userlist(ctx.author.name)
    userid = ctx.author.id
    ment = ctx.author.mention
    embedVar = discord.Embed(title=f'Watch List', description=f"Stocks {ment} likes!", color=0x00ff00)
    for t in user_list.keys():
        embedVar.add_field(name=t, value=user_list[t], inline=False)
    embedVar.set_footer(text="Cheers!!")
    await ctx.channel.send(embed=embedVar)

@client.command(name='add', help='Use #add to add a ticker symbol from your WL.')
async def add(ctx, ticker):
    await ctx.channel.send(yfi.add_userlist_item(ctx.author.name, ticker))

@client.command(name='delete', help='Use #delete to remove a ticker symbol from your WL.')
async def delete(ctx, ticker):
    await ctx.channel.send(yfi.del_userlist_item(ctx.author.name, ticker))

@add.error
async def add_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send('add command requires the ticker symbol.')   

@delete.error
async def del_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send('delete command requires the ticker symbol.')       

## Run the client 
client.run(cfg.Discord['token'])

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.lower().startswith('q!'):
#         t = message.content.split(":")[1]
#         resp = yfi.get_ticker(ticker=t)
#         await message.channel.send(resp)
    
#     if message.content.lower().startswith('div!'):
#         d = message.content.split(" ")[1]
#         div = yfi.get_dividend(ticker=d)
#         await message.channel.send(div)
