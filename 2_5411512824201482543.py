import requests
from telebot import types
import telebot
from time import sleep
import random
token = input(" [~] Enter Token : ")
bot = telebot.TeleBot(token)
r=requests.session() 
check = types.InlineKeyboardButton(text ="- Search", callback_data = 'check')
@bot.message_handler(commands=['بحث'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 1
    maac.add(check)
    bjj = message.chat.id
    bot.send_message(message.chat.id,text=f"""<strong>
Hi <code>{fr}</code>, 
- - - - - - - - - - 
Welcome Youtube Search Bot
Click Search. 
- - - - - - - - - - 
By  : @UX4SL 
</strong>
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == 'check':
    	trakos(call.message)
    if call.data == 'back':
    	baa(call.message)
def trakos(message):
	bot.send_message(message.chat.id,"ارسل اي شيء للبحث عنة")
@bot.message_handler(func=lambda m:True)
def sa(message):
	msg = message.text
	url = f'https://google7x.ml/API/SearchYtube.php?search={msg}'
	ref = requests.get(url)
	res = ref.json()
	gen = res['results'][0]['title']
	User = res['results'][0]['url']
	id = res['results'][0]['view']
	time = res['results'][0]['time']
	image = res['results'][0]['image']
	bot.send_message(message.chat.id,text=f'True ✅:\nName : {gen}\nURL : https://youtu.be/{User}\nView : {id}\nTime : {time}\nBy @UX4SL | @ESXAN')
	bot.send_photo(message.chat.id,image)
pass
#داشوفك تريد تخمط
bot.polling(True)