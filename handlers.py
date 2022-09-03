from telegram import Update
from telegram.ext import MessageHandler, CommandHandler, Filters
from settings import WELCOME_MESSAGE, TEAM_LEADS_CHAT_ID


def start(update: Update, context):
    update.message.reply_text(f'{WELCOME_MESSAGE.format(update.effective_user.full_name)}')


def forward_to_leads(update: Update, context):
    update.message.forward(chat_id=TEAM_LEADS_CHAT_ID)


def setup_dispatcher(dispatcher):
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(
        MessageHandler(Filters.chat_type.private, forward_to_leads)
    )
    return dispatcher
