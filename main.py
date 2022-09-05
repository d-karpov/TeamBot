from telegram.ext import Updater
from settings import TOKEN, PORT, APP_NAME_HEROKU
from handlers import setup_dispatcher
from bot_setup import bot_setup

updater = Updater(TOKEN)
dispatcher = updater.dispatcher
dispatcher = setup_dispatcher(dispatcher)
bot_setup()

if not APP_NAME_HEROKU:
    updater.start_polling()
    print('Local test mode is started')
else:
    updater.start_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=TOKEN,
            webhook_url=f"https://{APP_NAME_HEROKU}.herokuapp.com/{TOKEN}"
        )
updater.idle()
