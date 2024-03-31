from pyrogram import Client, filters
from pyrogram.types import  InlineKeyboardMarkup, InlineKeyboardButton,CallbackQuery


join_button = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text= "چنل ما", url="https://t.me/persian_bomber")],
        [InlineKeyboardButton(text= "👮🏻بررسی عضویت", callback_data="joined")]
    ]
)


def join_checker(_, client, message):
    try:
        user_object = client.get_chat_member(chat_id= "persian_bomber", user_id= message.from_user.id)
        return not user_object.status == "left" or user_object.status == 'kicked'
    except Exception as e:
        print(e)
        message.reply_text("⚠️کاربر گرامی شما در کانال های ما عضو نیستید⚠️"
                           "\n برای استفاده از ربات باید در کانال های ما عضو باشید"
                           "\n\n لطفا در کانال های زیر عضو شوید🔴"
                           "\n\n پس از عضویت روی بررسی عضویت کلیک کنید",
                           reply_markup= join_button )      
join_filter = filters.create(join_checker)

@Client.on_callback_query()
def callback_handler(client , callback_query):
    if callback_query.data == "joined":
        try:
            user_object = client.get_chat_member(chat_id="persian_bomber", user_id=callback_query.from_user.id)
            callback_query.edit_message_text("عضویت با موفقیت انجام شد"
                                             "\n\n برای ادامه روی /start کلیک کنید")
            

            return not user_object.status == "left" or user_object.status == 'kicked'
        except Exception as e:
            print(e)
            callback_query.message.reply_text("⚠️کاربر گرامی شما در کانال های ما عضو نیستید⚠️"
                            "\n برای استفاده از ربات باید در کانال های ما عضو باشید"
                            "\n\n لطفا در کانال های زیر عضو شوید🔴"
                            "\n\n پس از عضویت روی بررسی عضویت کلیک کنید",
                            reply_markup= join_button )
            
