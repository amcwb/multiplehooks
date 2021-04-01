from discord.ext import commands

def before(bot: commands.Bot):
    """Changes the before invoke of bot to automatically register multiple
    before-invocation hooks.

    Args:
        bot (commands.Bot): The bot to change the before-invoke hook of.
    """
    bot._before_invokes = []

    async def invoke_caller(ctx):
        for hook in bot._before_invokes:
            try:
                await hook(ctx)
            except:
                pass

    bot._before_invoke = invoke_caller

    def before_invoke(coro):
        bot._before_invokes.append(coro)

    bot.before_invoke = before_invoke


def after(bot: commands.Bot):
    """Changes the after invoke of bot to automatically register multiple
    after-invocation hooks.

    Args:
        bot (commands.Bot): The bot to change the after-invoke hook of.
    """
    bot._after_invokes = []

    async def invoke_caller(ctx):
        for hook in bot._after_invokes:
            try:
                await hook(ctx)
            except:
                pass

    bot._after_invoke = invoke_caller

    def after_invoke(coro):
        bot._after_invokes.append(coro)

    bot.after_invoke = after_invoke

