import telebot

token= ""

bot =telebot.TeleBot(token)


@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, как дела?")

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'отлично':
        bot.send_message(message.chat.id, "Я рад за тебя")
    elif message.text.lower() == "плохо":
        bot.send_message(message.chat.id, "Что случилось?")
    else:
        bot.send_message(message.chat.id, "Я пока не умею отвечать на такие сообщения")



bot.polling(none_stop=True)