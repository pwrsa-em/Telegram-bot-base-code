from pyrogram import Client, filters
from pyrogram.types import Message
from plugins import join_handler
from plugins.start import main_button
 



@Client.on_message(filters.text & filters.regex(r"برگشت") & join_handler.join_filter)
def back_handler(client: Client , message: Message):
    message.reply_text("لطفا یکی از گزینه های زیر ⬇️را انتخاب کنید",
                                 reply_markup= main_button)
