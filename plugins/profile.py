from pyrogram import Client,filters
from pyrogram.types import Message
from plugins import join_handler
import json



@Client.on_message(filters.regex(r"👩🏻‍🦰پروفایل🧑🏻‍🦰") & join_handler.join_filter)
def profile_view (client: Client, message: Message):

# ! open json file and read user info
    user_id = message.from_user.id
    user_name = message.from_user.id
    with open("database/database.json", "r") as file:
        data = json.load(file)

# ! Matching user ID with database IDs
    if str(user_id) in data:
        login_date = data[str(user_id)]['login_date']
        login_clock = data[str(user_id)]['login_clock']
        message.reply_text("📅تاریخ شروع استفاده از ربات :\t\t\t"
                           f"{login_date}\n \n"
                           "⌚زمان شروع استفاده از ربات :\t\t\t"
                           f"{login_clock}\n \n"
                           "👤نام کاربری :\t\t\t"
                           f"{user_name}\n \n"
                           "آیدی عددی🆔:\t\t\t"
                           f"{user_id}\n \n"
                           )
        
    else:
        message.reply_text("حساب کاربری یافت نشد لطفاروی /start کلیک کنید")


   
    