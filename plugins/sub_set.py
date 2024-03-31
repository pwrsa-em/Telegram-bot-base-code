from pyrogram import Client,filters
from pyrogram.types import Message
from plugins import join_handler


@Client.on_message(filters.regex(r"🔗لینک زیر مجموعه گیری🔗") & join_handler.join_filter)
def create_bot_invite_link(client: Client, message: Message):
    message.reply_text("⛔این قسمت فعلا در دسترس نیست")