import os
from dotenv import load_dotenv

load_dotenv()

# Server host and port
SERVER_HOST = os.getenv('SERVER_HOST', '0.0.0.0')
SERVER_PORT = int(os.getenv('SERVER_PORT', 8000))
DEBUG = os.getenv('DEBUG', 'True') in ["True", "true", "1"]

# Telegram Bot API token (default: None)
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', None)

# Twilio account SID and auth token (default: None)
ACCOUNT_SID = os.getenv('ACCOUNT_SID', None)
AUTH_TOKEN = os.getenv('AUTH_TOKEN', None)

# The Twilio sandbox or own business number
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER', None)

# The facebook page id from your Facebook Messenger App
FACEBOOK_PAGE_ID = os.getenv('FACEBOOK_PAGE_ID', None)

# You Personal Zapier NLA API key for calendar management
ZAPIER_NLA_API_KEY = os.getenv('ZAPIER_NLA_API_KEY', None)

# OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Choose your model between gpt-3, gpt-3.5-turbo, gpt-4
SELECTED_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4')

# Temperature value for OpenAI language model
TEMPERATURE_VALUE = float(os.getenv('TEMPERATURE_VALUE', 0.7))

# DALL-E settings
IMAGE_SIZE = os.getenv('DALL-E_IMAGE_SIZE', '256x256')

# Chatbot name for generating responses
BOT_NAME = os.getenv('BOT_NAME', 'Lago')

# Use BabyAGI or not?
BABYAGI = os.getenv('USE_BABYAGI', 'False') in ["True", "true", "1"]

# Where to store conversation memories etc.
HISTORY_DIR = './history'

# TODO Numbers For testing purposes only, should be changed later
MEMORYCONFIG = {'K_contextual': 2, 'K_latest': 4}
