from telebot import TeleBot, types

TOKEN = '7600136426:AAFR1LWbiaOACU_NDdnj6J0Xb9SW7k5QLAg'

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='Welcome to TonPredictionMarket')

if __name__ == '__main__':
    bot.polling(none_stop=True)
