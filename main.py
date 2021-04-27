import telebot
import time
bot = telebot.TeleBot('1779127045:AAH-H8OK3xdMSEkzirr5CBiP1qZdtDHXQ-c')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Привет, я самый инновационный бот в мире, в будущем.. \n Но на данный момент я могу лишь распознать когда пользователь говорит "Привет", а так же рассылать Снафф или десткое порно по команде "го веселиться"')



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    f = open('text.txt', 'a',encoding="utf-8")
    f.write(str(message.from_user.id)+" "+str(message.from_user.first_name)+" "+str(message.from_user.last_name)+" "+ time.ctime(time.time())+": "+ message.text+"\n")
    f.close()
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    elif message.text.lower()=="го веселиться":
        bot.send_message(message.from_user.id,"https://www.youtube. com/watch?v=dQw4w9WgXcQ")
        bot.send_message(message.from_user.id, "Просто убери пробел после точки...")

    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')





bot.polling(none_stop=True)