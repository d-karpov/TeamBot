import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('.env_test')) if os.getenv('MODE') else load_dotenv(find_dotenv())

# Telegram settings
TOKEN = os.getenv('TOKEN')
TEAM_LEADS_CHAT_ID = int(os.getenv('TEAM_LEADS_CHAT_ID'))
BOT_USERNAME = os.getenv('BOT_USERNAME')
# Messages
WELCOME_MESSAGE = os.getenv('WELCOME_MESSAGE')
HELP_MESSAGE = os.getenv('HELP_MESSAGE')
USER_ID_MARK = os.getenv('USER_ID_MARK')
# Heroku settings
PORT = int(os.environ.get('PORT', '8443'))
APP_NAME_HEROKU = os.getenv("APP_NAME_HEROKU")
