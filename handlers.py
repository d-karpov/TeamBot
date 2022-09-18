from telegram import Update
from telegram.ext import MessageHandler, CommandHandler, Filters, CallbackContext
from settings import WELCOME_MESSAGE, TEAM_LEADS_CHAT_ID, BOT_USERNAME, HELP_MESSAGE, USER_ID_MARK, HELP_COMMANDS


def start(update: Update, context: CallbackContext):
    message = update.message.reply_text(f'{WELCOME_MESSAGE.format(update.effective_user.full_name)}')
    context.bot.pin_chat_message(
        chat_id=update.message.chat_id,
        message_id=message.message_id
    )


def help(update: Update, context: CallbackContext):
    if update.effective_chat.type == 'supergroup':
        update.message.reply_text(
            f'{HELP_MESSAGE}\n'
            f'This chat ID - "{update.effective_chat.id}"\n'
            f'{HELP_COMMANDS}'
        )
    else:
        update.message.reply_text(HELP_MESSAGE)


def forward_to_leads(update: Update, context: CallbackContext):
    forwarded = update.message.forward(chat_id=TEAM_LEADS_CHAT_ID)
    if not forwarded.forward_from:
        context.bot_data[update.message.from_user.id] = update.message.from_user.full_name
        context.bot.send_message(
            chat_id=TEAM_LEADS_CHAT_ID,
            text=f'{update.message.from_user.name}:\n'
                 f'{forwarded.text}\n\n'
                 f'{USER_ID_MARK}\n'
                 f'{update.message.from_user.id}'
        )
        context.bot.delete_message(
            chat_id=TEAM_LEADS_CHAT_ID,
            message_id=forwarded.message_id
        )


def reply_to_teammate(update: Update, context: CallbackContext):
    user_id = None
    if update.message.reply_to_message.forward_from:
        user_id = update.message.reply_to_message.forward_from.id
    elif USER_ID_MARK in update.message.reply_to_message.text:
        try:
            user_id = int(update.message.reply_to_message.text.split('\n').pop())
        except ValueError:
            user_id = None
    if user_id:
        context.bot.copy_message(
            message_id=update.message.message_id,
            chat_id=user_id,
            from_chat_id=update.message.chat_id
        )


def get_users(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'{context.bot_data}'
    )


def send_to_all(_, context: CallbackContext):
    for user_id in context.bot_data.keys():
        context.bot.send_message(
            chat_id=user_id,
            text=' '.join(context.args)
        )


def setup_dispatcher(dispatcher):
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('get_users', get_users, Filters.chat(TEAM_LEADS_CHAT_ID)))
    dispatcher.add_handler(CommandHandler('send_to_all', send_to_all, Filters.chat(TEAM_LEADS_CHAT_ID)))

    dispatcher.add_handler(
        MessageHandler(Filters.chat_type.private & (~Filters.user(username=BOT_USERNAME) & (~Filters.command)),
                       forward_to_leads)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.reply & Filters.chat(TEAM_LEADS_CHAT_ID), reply_to_teammate)
    )

    return dispatcher
