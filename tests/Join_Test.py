from discord.ext.commands import context
from util import util
async def join_test(ctx: context):
    await util.print_and_send(ctx, "I am join test")