from pyrogram import Client, filters
from pyrogram.types import Message,ReplyKeyboardMarkup,CallbackQuery
from plugins import join_handler



@Client.on_message(filters.text & filters.regex(r"🔛سرویس های فعال🔛") & join_handler.join_filter)
def service_handler(client: Client , message: Message):
    message.reply_text("⬇️یکی از سرویس های زیر را انتخاب کنید⬇️",
                            reply_markup= ReplyKeyboardMarkup(
                                [
                                    ["💥سرویس نامحدود 1💥","💥سرویس نامحدود 2💥"],
                                    ["🆓سرویس رایگان 3🆓","🆓سرویس رایگان 2🆓","🆓سرویس رایگان 1🆓"],
                                    ["🆓سرویس رایگان 5🆓","🆓سرویس رایگان 4🆓"],
                                    ["برگشت"]
                                ],
                            ),
                        )

