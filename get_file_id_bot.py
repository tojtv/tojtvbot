import telebot

# ✅ Инҷо токени боти худро гузор
TOKEN = '7514528609:AAHg5my4UEEtmA6BtCyznlZJAr0orC8tx8Y'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Салом! Видеоро фирист, ман ба ту File ID медиҳам.")

@bot.message_handler(content_types=['video'])
def get_file_id(message):
    file_id = message.video.file_id
    bot.send_message(message.chat.id, f"🎬 File ID-и шумо:\n\n{file_id}")

bot.polling()
