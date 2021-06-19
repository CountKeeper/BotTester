from discord.ext.commands import context
async def print_and_send(ctx: context, message: str):
    print(message)
    await ctx.send(message)