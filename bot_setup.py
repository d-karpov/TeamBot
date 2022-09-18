from telegram import Bot, BotCommandScopeChatAdministrators
from settings import TOKEN, TEAM_LEADS_CHAT_ID

bot = Bot(TOKEN)


def bot_setup():
    bot.set_my_commands(
        [
            ['start', 'Starts bot, pins small instruction'],
            ['help', 'About']
        ]
    )
    bot.set_my_commands(
        [
            ['help', 'About'],
            ['get_users', 'Get all users who sends messages to bot']
        ],
        scope=BotCommandScopeChatAdministrators(chat_id=TEAM_LEADS_CHAT_ID)
    )
