import telebot
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN') 
bot = telebot.TeleBot(BOT_TOKEN)

SHOP_NAME = "Bismillah General Store"
MALIK = "Haji Sahab"
TIMING = "Subah 9 se Raat 11"
EASYPAISA = "03xx-xxxxxxx"
MAPS = "https://maps.app.goo.gl/xxxx"

MENU = f"""
*{SHOP_NAME}* 🛒
Malik: {MALIK}
Timing: {TIMING}

*Menu:*
1. Chai - 60 Rs
2. Paratha - 40 Rs  
3. Coke - 100 Rs
4. Biscuit - 30 Rs
5. Cigarette - 280 Rs

Order ke liye item ka naam likho 👇
Easypaisa: {EASYPAISA}
Location: {MAPS}
"""

@bot.message_handler(commands=['start', 'menu'])
def start(msg):
    bot.reply_to(msg, f"Assalam o Alaikum {msg.from_user.first_name}!\n\n{MENU}", parse_mode='Markdown')

@bot.message_handler(func=lambda m: True)
def order(msg):
    bot.reply_to(msg, f"Order mil gaya: *{msg.text}*\n\n{MALIK} ko bhej diya. 10 min mein delivery.\nJazakAllah!", parse_mode='Markdown')

print(f"{SHOP_NAME} ka bot start")
bot.polling()
