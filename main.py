from telegram.ext import Updater
from settings import TOKEN, PORT, APP_NAME_HEROKU
from handlers import setup_dispatcher


updater = Updater(TOKEN)
dispatcher = updater.dispatcher
dispatcher = setup_dispatcher(dispatcher)
updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"https://{APP_NAME_HEROKU}.herokuapp.com/{TOKEN}"
    )
updater.idle()
