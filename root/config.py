"""
© Mrvishal2k2
RenameBot
This file is a part of mrvishal2k2 rename repo
Dont kang !!!
© Mrvishal2k2
"""
import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", "8813038"))
    API_HASH = os.environ.get("API_HASH", "780fd96b159baa710dada78ff1621b54")
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5708128216:AAFmjBLGKcJMp86dKawfZX5qBMPVc1U-2Lc")
    AUTH_USERS = [int(x) for x in os.environ.get("AUTH_USERS", "").split()]
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./bot/DOWNLOADS")
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://manju:manju@cluster0.ufpy5w1.mongodb.net/?retryWrites=true&w=majority")
    # owner is for log cmd only owner can use (this can be multiple users)
    OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID", "2083503061")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "bhatmanju")
    CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", False)
