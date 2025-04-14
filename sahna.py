import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔑 Токени бот
TOKEN = '7838164542:AAF7hybu9St7G_jR-Yhea2v7hTKCvZbBxoA'
bot = telebot.TeleBot(TOKEN)

# 📢 Канал барои санҷиши обуна
REQUIRED_CHANNEL = '@tojmusic'

# 🎬 File ID-и филми "Деҳаи гумшуда"
VIDEO_FILE_ID = 'BAACAgIAAxkBAAMCZ_wv-aIXUE3mwXVS3ciNQYOsxq8AAkBtAAIgSOFLydnJ2EvjWe02BA'

# 🔍 Санҷиши обуна

def check_subscription(user_id):
    try:
        status = bot.get_chat_member(REQUIRED_CHANNEL, user_id).status
        if status in ['left', 'kicked']:
            return False
    except:
        return False
    return True

# 🟢 Командаи /start бо ду тугма: "Деҳаи гумшуда" ва "Саҳна"
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("🎬 Деҳаи гумшуда", callback_data='deha'),
        InlineKeyboardButton("📺 Силсилафилми Саҳна", callback_data='sahna')
    )
    bot.send_message(message.chat.id, "Салом! Филмеро интихоб кун:", reply_markup=markup)

# 🎬 Callback барои "Деҳаи гумшуда"
@bot.callback_query_handler(func=lambda call: call.data == 'deha')
def send_video(call):
    user_id = call.from_user.id
    if check_subscription(user_id):
        bot.send_message(call.message.chat.id, "🎬 Филми 'Деҳаи гумшуда':")
        bot.send_video(call.message.chat.id, VIDEO_FILE_ID)
    else:
        bot.send_message(call.message.chat.id, "📛 Барои дидани филм, аввал ба канали зерин обуна шав:\n👉 @tojmusic\n\n✅ Баъд тугмаро боз зер кун.")

# 📺 Callback барои "Силсилафилми Саҳна"
@bot.callback_query_handler(func=lambda call: call.data == 'sahna')
def send_sahna_channel_link(call):
    user_id = call.from_user.id
    if check_subscription(user_id):
        bot.send_message(call.message.chat.id, "📺 Барои тамошо гузар ба канали 'Саҳна':\n👉 https://t.me/+0O6EhRuiKWoyNjgy")
    else:
        bot.send_message(call.message.chat.id, "📛 Барои дидани силсилафилм, аввал ба канали зерин обуна шав:\n👉 @tojmusic\n\n✅ Баъд тугмаро боз зер кун.")

# ▶️ Оғози бот
bot.polling()
