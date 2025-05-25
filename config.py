# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper



import os

class Config:
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", ")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", ")
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
