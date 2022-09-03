import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')

TEAM_LEADS_CHAT_ID = os.getenv('TEAM_LEADS_CHAT_ID')

WELCOME_MESSAGE = os.getenv('WELCOME_MESSAGE')
