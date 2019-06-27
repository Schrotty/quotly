from dotenv import load_dotenv, find_dotenv
from discord.ext import commands
from quotly.Quotly import Quotly

load_dotenv(find_dotenv())
quotly = Quotly()
quoty_bot = commands.Bot(command_prefix='!')

cmds = {
    'add_quote': 'quotly-add',
    'get_quote': 'quotly-get'
}


@quoty_bot.command(name=cmds['add_quote'])
async def create(ctx, q, *targets):
    quotly.store_quote(q, targets)

    await ctx.send('nothing')


@quoty_bot.command(name=cmds['get_quote'])
async def quote(ctx, *targets):
    if not targets:
        await ctx.send(quotly.fetch_quote())
    else:
        await ctx.send(quotly.fetch_quote(targets))
