from pyrogram import Client,filters
from pyrogram.types import Message
from plugins import join_handler 

help_message ="⚠️قبل از استفاده از ربات به بخش قوانین سر بزنید⚠️\n"\
                   "با ثبت درخواست بمبر رایگان، پیام های ثبت نام از طرف سایت های مختلف برای شماره هدف ارسال میشود. 💣\n"\
                   " _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"\
                   "سرویس های رایگان دارای محدودیت هستند،یعنی در ارسال پیامک ها محدودیت تعداد دارن و بیش از یک تعداد خاص برای شماره هدف پیامک ارسال میشود🔱\n"\
                   " _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"\
                   "برای ارسال نامحدود پیامک باید اشتراک VIP تهیه کنید و با استفاده از سرویس نامحدود میتوانید به صورت دلخواه پیامک ارسال کنید 🔰\n"\
                   " _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"\
                   "راهنمای سرویس ها 📚 :\n"\
                   "1 : با سرویس نامحدود 1 میتوانید با تعداد دلخواه پیامک ارسال کنید\n"\
                   "2 : با استفاده از سرویس نامحدود 2 میتوانید با زمان دلخواه پیامک ارسال کنید\n"\
                   "✅ نمونه (دقیقه): 60\n"\
                   " _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"\
                   "راهنمای استفاده 📚 :\n"\
                   "1 : در بخش سرویس های بمبر یک سرویس را انتخاب کنیدvip یا free . \n"\
                   "2 : بعد از ارسال پیامک به سمت شماره هدف ارسال بعدی به همان شماره 5 دقیقه بعد انجام میشود\n"\
                   "3 : شماره کاربر مورد نظر رو به درستی وارد کنید و صبر کنید که ربات تایید رو ارسال کند,شماره باید بدون 0 و بدون هیچ فاصله ای\n"\
                   "✅ نمونه : 9123456789\n"\
                   " _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"\
                   "♨️ Sms Bomber یا اسمس بمبر چیست؟\n"\
                   "➖➖➖➖➖➖➖➖\n"\
                   "🌀 اس ام اس بمبر روشی هست که هکرها برای ارسال بی نهایت اس ام اس (پیامک) کال (تلفن) به یک یا چند شماره تلفن استفاده میکنند در این روش از آسیب پذیری یک یا چند برنامه سوءاستفاده میشود و یا هکر با کمک یک پنل پیامکی این کار را انجام میدهد. و شناسایی کسی که این پیامک ها را ارسال میکند غیر ممکن است . . . ! ♨️\n"\
                   "به راحتی میتوانید بدخواهتون رو اذیت کنید ⭕️\n"\
                   "🔰 تلفن های همراه از سرویس پیام کوتاه یا پیام کوتاه برای ارسال پیام های متنی استفاده می کنند.\n"\
                   "➖➖➖➖➖➖➖➖\n" \
                   "📢کانال اطلاع رسانی ربات⬇️\n"\
                   "@persian_bomber"

@Client.on_message(filters.regex(r"📑راهنما📑") & join_handler.join_filter)
def helper(client: Client, message: Message):
    message.reply_text(help_message)
