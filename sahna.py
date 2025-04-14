import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔑 Токени боти ту
TOKEN = '7838164542:AAF7hybu9St7G_jR-Yhea2v7hTKCvZbBxoA'
bot = telebot.TeleBot(TOKEN)

# 📢 Канале, ки истифодабаранда бояд обуна шавад
REQUIRED_CHANNEL = '@tojmusic'

# 🔎 Функсия барои санҷидани обуна

def check_subscription(user_id):
    try:
        status = bot.get_chat_member(REQUIRED_CHANNEL, user_id).status
        if status in ['left', 'kicked']:
            return False
    except:
        return False
    return True

# 🟢 Фармони /start бо тугмаи "Саҳна"
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📺 Силсилафилми Саҳна", callback_data='sahna'))
    bot.send_message(message.chat.id, "Салом! Барои дидани силсилафилм тугмаро зер кун:", reply_markup=markup)

# 📺 Callback барои тугмаи "Саҳна"
@bot.callback_query_handler(func=lambda call: call.data == 'sahna')
def send_sahna_channel_link(call):
    user_id = call.from_user.id
    if check_subscription(user_id):
        bot.send_message(call.message.chat.id, "📺 Барои тамошо гузар ба канали 'Саҳна':\n👉 https://t.me/+0O6EhRuiKWoyNjgy")
    else:
        text = "📛 Барои дидани силсилафилм, аввал ба канали зерин обуна шав:\n👉 @tojmusic\n\n✅ Баъд тугмаро боз зер кун."
        bot.send_message(call.message.chat.id, text)

# ▶️ Оғози бот
bot.polling()
