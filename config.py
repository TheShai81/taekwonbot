'''Configuration file for API tokens and guild names.'''

from dotenv import load_dotenv
import os

# load env variables
load_dotenv()

TOKEN = os.getenv("DISCORD_API_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")