from telegram import Bot, BotCommandScopeAllGroupChats
from settings import TOKEN

bot = Bot(TOKEN)


def bot_setup():
    bot.set_my_commands(
        [
            ['start', 'Starts bot, pins small instruction'],
            ['help', 'About']
        ],
    )
