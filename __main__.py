from pyrogram import Client
import os

plugins = dict(root = "plugins")
API_ID = int(os.environ.get("API_ID" , 12345678))
API_HASH = os.environ.get("API_HASH" , "parsa esmaili")
BOT_TOKEN = os.environ.get("BOT_TOKEN" , "pwrsa_em")

app = Client(
    "sms_bomber",
    api_hash= API_HASH,
    api_id= API_ID,
    bot_token= BOT_TOKEN,
    plugins= plugins
    )

app.run()