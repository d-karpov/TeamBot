from telegram.ext import Updater
from settings import TOKEN
from handlers import setup_dispatcher


updater = Updater(TOKEN)
dispatcher = updater.dispatcher
dispatcher = setup_dispatcher(dispatcher)
updater.start_polling()
updater.idle()
