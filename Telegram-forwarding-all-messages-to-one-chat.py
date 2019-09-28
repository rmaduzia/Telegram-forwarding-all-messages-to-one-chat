import telebot  # importing pyTelegramBotAPI library

token=''  #telegram bot api token

bot = telebot.TeleBot(token)

chat_id_main="" #chat id to which messages will be forwarded


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if str(message.chat.id) != chat_id_main:
        bot.send_message(chat_id_main, text=message.text)


bot.polling()



