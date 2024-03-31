from pyrogram import Client,filters
from pyrogram.types import Message,ReplyKeyboardMarkup
from collections import defaultdict
from plugins import join_handler
from datetime import datetime
import json


def Tree():
    return defaultdict(Tree)
user_pocket = Tree()


main_button = ReplyKeyboardMarkup(
            [
                ["🔛سرویس های فعال🔛"],
                ["🔗لینک زیر مجموعه گیری🔗","👩🏻‍🦰پروفایل🧑🏻‍🦰"],
                ["💥VIP💥","📑راهنما📑"],
                ["🎧درخواست پشتیبانی🎧"]
            ],
            resize_keyboard= True,
        )
login_date = datetime.now().strftime("%Y/%m/%d")
login_clock = datetime.now().strftime("%H:%M:%S")


@Client.on_message(filters.command("start") & join_handler.join_filter)
async def wellcome_massege(client: Client, message: Message):
    user_id = message.from_user.id

    if user_pocket[user_id]["step"] == 1:
# ! message when member logined and second request
        await message.reply_text("لطفا یکی از گزینه های زیر ⬇️را انتخاب کنید",
        reply_markup= main_button)
        

    else :
# ! save member login Time
        with open("database/database.json" , "r+") as file:
            user_db = json.load(file)
            if str(user_id) not in user_db:
                user_db[user_id] = {"login_date" : login_date ,
                "login_clock" : login_clock}
                file.seek(0)
                json.dump(user_db , file , indent= 4)

                
# ! user wellcome Message
        user_name = message.from_user.first_name
        wellcome_massege = f"سلام {user_name} عزیز "\
                            "\n\n\tبه ربات بمبر ما خوش آمدید💣" \
                            "\n\n\t لطفا یکی از گزینه های زیر ⬇️را انتخاب کنید"   
        await message.reply_text(
            wellcome_massege,
            reply_markup= main_button
        )
        user_pocket[user_id]["step"] = 1