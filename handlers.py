from telegram import Update
from telegram.ext import MessageHandler, CommandHandler, Filters, CallbackContext
from settings import WELCOME_MESSAGE, TEAM_LEADS_CHAT_ID, BOT_USERNAME


def start(update: Update, context: CallbackContext):
    message = update.message.reply_text(f'{WELCOME_MESSAGE.format(update.effective_user.full_name)}')
    context.bot.pin_chat_message(
        chat_id=update.message.chat_id,
        message_id=message.message_id
    )


def help(update: Update, context: CallbackContext):
    update.message.reply_text()


def forward_to_leads(update: Update, context: CallbackContext):
    update.message.forward(chat_id=TEAM_LEADS_CHAT_ID)


def reply_to_teammate(update: Update, context: CallbackContext):
    if update.message.reply_to_message.forward_from:
        user_id = update.message.reply_to_message.forward_from.id
        context.bot.copy_message(
            message_id=update.message.message_id,
            chat_id=user_id,
            from_chat_id=update.message.chat_id
        )


def setup_dispatcher(dispatcher):
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler(['help', 'h'], help))

    dispatcher.add_handler(
        MessageHandler(Filters.chat_type.private & (~Filters.user(username=BOT_USERNAME)), forward_to_leads)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.reply & Filters.chat(TEAM_LEADS_CHAT_ID), reply_to_teammate)
    )
    return dispatcher
