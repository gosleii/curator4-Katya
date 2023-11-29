import telebot

bot = telebot.TeleBot('6717867395:AAH-zuj0RqOhSoRUUthcZ0fYMQHz2l_iqSk')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, {username}! Я - бот. Могу погадать тебе. Введи команду /guess', parse_mode='Markdown')


@bot.message_handler(commands=['help'])
def help_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Я не могу предсказывать будущее, так как я всего лишь компьютерная программа.")


bot.infinity_polling()