import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "11472991"))
API_HASH = os.environ.get("API_HASH", "c78c50d54baf2173e8b3f75c359c0c72")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7645182647:AAFGpYGhUKarmyLY4iY17hkPBpCmcGLdgTw")
ADMIN = int(os.environ.get("ADMIN", "1430742022"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "-1002298937998")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002318167392"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sakthirajbaskaran:gqJb3gPWMc4GqhYB@ani-tubez.ctim8nc.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "TechifyBots")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://envs.sh/Qrd.jpg")
