from telegram.ext import Updater, MessageHandler,Filters
from Adafruit_IO import Client
import os

aio = Client('Preethi__',os.getenv('Preethi__'))
def turn_on_light(bot,update):
    aio.send('bedroom-light',1)
    data = aio.receive('bedroom-light')
    print(f'Received value:{data.value}')
    chat_id=bot.message.chat_id
    path='https://i.pinimg.com/originals/bb/d8/86/bbd886fdc6abd7d6d51160687047aee8.jpg'
    bot.message.reply_text('light is turned on')
    update.bot.sendPhoto(chat_id=chat_id,photo=path)
def turn_off_light(bot,update):
    aio.send('bedroom-light',0)
    data = aio.receive('bedroom-light')
    print(f'Received value:{data.value}')
    chat_id=bot.message.chat_id
    path='https://i.pinimg.com/474x/77/6a/30/776a3077389d21a1669a02a15acaa777.jpg'
    bot.message.reply_text('light is turned off')
    update.bot.sendPhoto(chat_id=chat_id,photo=path)
def turn_on_fan(bot,update):
    aio.send('fan',1)
    data = aio.receive('fan')
    print(f'Received value:{data.value}')
    chat_id=bot.message.chat_id
    path='https://pursolaraz.com/wp-content/uploads/2019/04/Depositphotos_1175497_l-2015-1080.jpg'
    bot.message.reply_text('fan is turned on')
    update.bot.sendPhoto(chat_id=chat_id,photo=path)
def turn_off_fan(bot,update):
    aio.send('fan',0)
    data = aio.receive('fan')
    print(f'Received value:{data.value}')
    chat_id=bot.message.chat_id
    path='https://images-na.ssl-images-amazon.com/images/I/51YbI23n0NL._SX679_.jpg'
    bot.message.reply_text('fan is turned off')
    update.bot.sendPhoto(chat_id=chat_id,photo=path)
def main(bot,update):
      a = bot.message.text
      print(a)

      if a=="turn on light":
        turn_on_light(bot,update)
      elif a=="turn off light" or a=="light off":
          turn_off_light(bot,update)
      elif a=="turn on fan":
          turn_on_fan(bot,update)
      elif a=="turn off fan" or a=="fan off":
          turn_off_fan(bot,update)
      else:
            bot.message.reply_text('invalid')

BOT_TOKEN = os.getenv('BOT_TOKEN')  
u = Updater(BOT_TOKEN,use_context = True) 
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main)) 
u.start_polling()
u.idle()
