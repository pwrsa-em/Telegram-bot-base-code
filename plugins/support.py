from pyrogram import Client,filters
from pyrogram.types import Message,ReplyKeyboardMarkup
from plugins import join_handler,start

support_message= "👮🏻 تیم پشتیبانی در خدمت شما هستن\n\n"\
                 "• بعد از درخواست پشتیبانی ،پشتیبان فعال درخواست شما را پیگیری میکند\n\n"\
                 "• لطفا پیام، سوال، پیشنهاد و یا انتقاد خود را در ارسال کنید"
back_button = ReplyKeyboardMarkup(
    [
        ["برگشت"]
    ],
    resize_keyboard= True
)


@Client.on_message(filters.regex(r"🎧درخواست پشتیبانی🎧") & join_handler.join_filter)
async def support_handler(client:Client, message:Message):
    user_name = message.from_user.username 
    try:
        # !send message on channel
        await client.send_message(181974063,
                                text= f"@{user_name}: {message.text}")
        await message.reply_text("درخواست شما با موفقیت به پشتیبان ارسال شد.")

    except Exception as e:
        # !send message feild
        await message.reply_text(f"متأسفانه مشکلی در درخواست پشتیبانی رخ داده است. لطفا دوباره امتحان کنید. خطا: {e}")