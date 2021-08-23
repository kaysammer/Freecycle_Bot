import telegram
import sys
firstarg=sys.argv[1]
bot = telegram.Bot(token='TOKEN')
#print(bot.get_me())
updates = bot.get_updates()
#print(updates[0])
bot.send_message(text=firstarg, chat_id=1306478246)