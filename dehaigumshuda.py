import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔑 Токени боти нав
TOKEN = '7838164542:AAF7hybu9St7G_jR-Yhea2v7hTKCvZbBxoA'
bot = telebot.TeleBot(TOKEN)

# 📢 Каналҳое, ки истифодабаранда бояд обуна шавад
REQUIRED_CHANNELS = ['@tojserie', '@tojmusic']

# 🎬 File ID-и видео
VIDEO_FILE_ID = 'BAACAgIAAxkBAAMCZ_wv-aIXUE3mwXVS3ciNQYOsxq8AAkBtAAIgSOFLydnJ2EvjWe02BA'

# 🔎 Санҷиши обуна
def check_subscription(user_id):
    for channel in REQUIRED_CHANNELS:
        try:
            status = bot.get_chat_member(channel, user_id).status
            if status in ['left', 'kicked']:
                return False
        except:
            return False
    return True

# 🟢 Қабули фармони /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🎬 Деҳаи гумшуда", callback_data='deha'))
    bot.send_message(message.chat.id, "Салом! Барои дидани филм тугмаро зер кун:", reply_markup=markup)

# 🎬 Callback барои тугма
@bot.callback_query_handler(func=lambda call: call.data == 'deha')
def send_video_if_subscribed(call):
    user_id = call.from_user.id
    if check_subscription(user_id):
        bot.send_message(call.message.chat.id, "🎬 Филми 'Деҳаи гумшуда':")
        bot.send_video(call.message.chat.id, VIDEO_FILE_ID)
    else:
        text = "📛 Барои дидани филм, аввал ба каналҳои зерин обуна шав:\n\n"
        for ch in REQUIRED_CHANNELS:
            text += f"👉 {ch}\n"
        text += "\n✅ Пас аз обуна шудан, тугмаро боз зер кун."
        bot.send_message(call.message.chat.id, text)

bot.polling()
