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
@client.command(name='quote', help='Use #quote symbol to view the most recent quote.')
async def quote(ctx, ticker):
    q = yfi.get_quote(ticker)
    q_info = q.info
    embedVar = discord.Embed(title=f'{q_info.get("longName")} [{q_info.get("symbol")}]', description = "_**Summary**_",color=0x052d68)
    embedVar.add_field(name= "Price", value= f'Previous Close: `{round(q_info.get("previousClose"), 2)}`\n' 
                                             f'Market Open: `{q_info.get("regularMarketOpen")}`\n' 
                                             f'Current Price: `{round(q_info.get("currentPrice"), 2)}`\n ', inline=True)    
    embedVar.set_thumbnail(url= q_info.get('logo_url'))
    embedVar.set_footer(text="Good luck with your stock picks.")
    await ctx.channel.send(embed=embedVar)


@client.command(name='list', help='Use #list to view the stocks in your WL.')
async def list(ctx):
    user_list = yfi.get_userlist(ctx.author.name)
    userid = ctx.author.id
    ment = ctx.author.mention
    embedVar = discord.Embed(title=f'Watch List', description=f"Stocks {ment} likes!", color=0x00ff00)
    embedVar.set_thumbnail(url='https://stockbotimages.s3.us-east-2.amazonaws.com/stock_cs_chart.png')
    # embedVar.from_dict(user_list)
    # print(user_list)
    for t in user_list.keys():
        embedVar.add_field(name=t, value=user_list[t], inline=False)
    embedVar.set_footer(text="Good luck with your stock picks.")
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
    if isinstance(error, commands.CommandInvokeError) and str(error).find("shortName") > 0 :
        await ctx.channel.send('Invalid ticker symbol.')

@delete.error
async def del_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send('delete command requires the ticker symbol.')       

## Run the client 
client.run(cfg.Discord['token'])
