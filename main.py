import time
from telebot import TeleBot, types

TOKEN ='7600136426:AAFR1LWbiaOACU_NDdnj6J0Xb9SW7k5QLAg'
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = """
*Hello world\!*

Mini\-app: lower left corner \n\n [Channel](https://t.me/tonpredictionmarket) 

The ability to simulate situations about the resolution of reality is a gift of man that distinguishes him from primates\. We hereby want to start our breathtaking journey where probabilities are no longer abstract definitions\. ☀️

Taking into account the highly\-alpha version of our TMA, we want to prevent you from making some mistakes while using our app:

✏️ Having accepted transaction in your wallet DO NOT cancel it in mini\-app while using desktop version of telegram\.

❌ DO NOT go for broke\. Please, consider all the risks associated with an early version of our product\. It’s alpha test \- use the amount of TON that you don't mind losing \(and divide it by 3\)\.

We will keep you informed of our updates\! And special thanks to our lovely alpha testers 👥
"""

    small_text = """
    👇🏻Mini\-app: lower left corner
    """

    keyboard = types.InlineKeyboardMarkup()

    community_button = types.InlineKeyboardButton(text="Join Community", url="https://t.me/tonpredictionmarket")
    app_button = types.InlineKeyboardButton(text="Launch App", url="https://t.me/TonPredictionMarketBot?startapp")

    keyboard.add(app_button, community_button)

    video = open('IMG_4876.MP4', 'rb')
    bot.send_message(message.chat.id, welcome_text, parse_mode="MarkdownV2")
    bot.send_video(message.chat.id, video)
    bot.send_message(message.chat.id, small_text, parse_mode="MarkdownV2", reply_markup=keyboard)


@bot.message_handler(commands=['message'])
def send_launch_app_message(message):
    kb = types.InlineKeyboardMarkup()
    launch_app_button = types.InlineKeyboardButton(text="Launch App", url="https://t.me/TonPredictionMarketBot?startapp")
    kb.add(launch_app_button)
    bot.send_message(message.chat.id, "button to launch app:", reply_markup=kb)

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=100)
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(15)
