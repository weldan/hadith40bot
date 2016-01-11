#!/usr/bin/python
import telegram
import logging

Updater = telegram.Updater

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
	answer = "Assalamualaikum. Sila taip /hadith [nombor] untuk mengetahui tentang hadith tersebut ikut turutan. contoh: /hadith 1"
	bot.sendMessage(chat_id = update.message.chat_id, text = answer)

def stop(bot, update):
	answer = "Terima kasih kerana menggunakan hadith 40 bot"
	bot.sendMessage(chat_id = update.message.chat_id, text = answer)

def hadith(bot, update):
	question = update.message.text.split()
	try:
		hadith_number = int(question[-1])
	except ValueError:
		bot.sendMessage(chat_id = update.message.chat_id, text = "Sila beri nombor hadith.")

	with open('hadith/hadith'+str(hadith_number)+'.txt', 'r') as myfile:
	    data=myfile.read()
	    bot.sendMessage(chat_id = update.message.chat_id, text = data, parse_mode=telegram.ParseMode.MARKDOWN)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
	updater = Updater(token = '170465132:AAEVtwxjATIEw5u-ajoK6cpz5gliiLpXPkU')
	dispatcher = updater.dispatcher

	dispatcher.addTelegramCommandHandler('start', start)
	dispatcher.addTelegramCommandHandler('stop', stop)
	dispatcher.addTelegramCommandHandler('hadith', hadith)

	updater.start_polling()

	updater.idle()

	updater.addErrorHandler(error)

if __name__ == "__main__":
	main()