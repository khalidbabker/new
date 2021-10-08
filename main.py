from telegram import *
from telegram.ext import *
from config import PORT,TOKEN
bot = Bot('2044919277:AAE1RUW1gi_wYQjohOBNFEpH2SCppygsljI')
updater = Updater('2044919277:AAE1RUW1gi_wYQjohOBNFEpH2SCppygsljI',use_context=True)
dispat = updater.dispatcher
def start(update:Update,context:CallbackContext):
	bot.send_message(chat_id=update.effective_chat.id,text='hello yaaa')
	context.bot.sendDocument(chat_id=update.effective_chat.id,document=open('a.pdf','rb'),timeout=120)
dispat.add_handler(CommandHandler('start',start))
print('bot is running.... ')
updater.start_webhook('0.0.0.0',PORT,TOKEN,webhook_url='https://botreal1.herokuapp.com/'+TOKEN)
updater.idle()