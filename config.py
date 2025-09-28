import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8347513002:AAG02qp0_dmTcrkiNCtyq2_cKFyy5Uo9kfM")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23948271"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "71c105c2ee890876b4ec4a8a898da783")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6853851676"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://jicitaf640_db_user:1saSbYRLlQOJqqj8@cluster0.yujacx3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
