# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper



import os

class Config:
    API_ID = os.environ.get("API_ID", "26614080")
    API_HASH = os.environ.get("API_HASH", "7d2c9a5628814e1430b30a1f0dc0165b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8017499587:AAHwx8VdtQsf83ujqKCF8xnByuT-8gLZrYk")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forward-bot")
    # Add error handling for DB_URL
    DB_URL = os.environ.get("DB_URL")
    if not DB_URL:
        raise ValueError("MongoDB connection string (DB_URL) is not set in environment variables")
    DB_NAME = os.environ.get("DB_NAME", "team_pbail")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '7641491740').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    






# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
