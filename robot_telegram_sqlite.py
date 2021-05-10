import sys
import time
from datetime import datetime
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
       if msg['text'] == '/start':
          bot.sendMessage(chat_id, '''به تنها ربات فروش بليت سينما خوش آمديد .\n از دستورات زير استفاده کنيد :\n
/site- my site very good
/animashen- film animashen
/fantezi- film fantezi
/varzesh- film varzeshi
/elmi- film elmi
/moaamai- film moaamai
/komedi- film komedi
/hemasi- film hemasi
/takhayoli- film takhayoli
/exit- with exit in robot''')
    if msg['text']=='/site':
        bot.sendMessage(chat_id, text='ورود به سايت :'+ 'https://cinematicket.org/')
    if msg['text']=='/animashen':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='/خردسال', callback_data='خردسال'),InlineKeyboardButton(text='/کودک', callback_data='کودک')],
            [InlineKeyboardButton(text='/نوجوان', callback_data='نوجوان'),InlineKeyboardButton(text='/جوان', callback_data='جوان')],
            [InlineKeyboardButton(text='/ميان سال', callback_data='ميان سال'),InlineKeyboardButton(text='/سالمند', callback_data='سالمند')],
            [InlineKeyboardButton(text='/خروج', switch_inline_query='خروج')],
            ])

        bot.sendMessage(chat_id, 'فيلم انيميشني خود را انتخاب کنيد  ', reply_markup=keyboard)



def on_callback_query(msg):
    cnn= sqlite3.connect('sans_robot.db')
    cur= cnn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
    id TEXT,
    sans TEXT,
    time TEXT,
    code TEXT);
    ''')#INT PRIMARY KEY
    cnn.commit()

    
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data, datetime.now())

    text='نوبت شما ثبت شد '
    bb=('زمان رزرو نوبت شما : '+str(datetime.now()))
    cc=('\nشماره پيگيري '+query_id)
    if query_data == 'خردسال':
       bot.sendMessage(from_id, text=('نوبت شما در خردسال ثبت شد :\n')+(bb)+(cc))
       a=[(from_id,query_data,str(datetime.now()),query_id)]
       cur.executemany('insert into users(id,sans,time,code) values(?,?,?,?)',a)
       cnn.commit()
       cnn.close()
       
    if query_data == 'کودک':
       bot.sendMessage(from_id, text=('نوبت شما در کودک ثبت شد :\n')+(bb)+(cc))
       b=[(from_id,query_data,str(datetime.now()),query_id)]
       cur.executemany('insert into users(id,sans,time,code) values(?,?,?,?)',b)
       cnn.commit()
       cnn.close()
       
    if query_data == 'نوجوان':
       bot.sendMessage(from_id, text=('نوبت شما در نوجوان ثبت شد :\n')+(bb)+(cc))
       c=[(from_id,query_data,str(datetime.now()),query_id)]
       cur.executemany('insert into users(id,sans,time,code) values(?,?,?,?)',c)
       cnn.commit()
       cnn.close()
       
    if query_data == 'جوان':
       bot.sendMessage(from_id, text=('نوبت شما در جوان ثبت شد :\n')+(bb)+(cc))
       d=[(from_id,query_data,str(datetime.now()),query_id)]
       cur.executemany('insert into users(id,sans,time,code) values(?,?,?,?)',d)
       cnn.commit()
       cnn.close()
       
    if query_data == 'ميان سال':
       bot.sendMessage(from_id, text=('نوبت شما در ميانسال ثبت شد :\n')+(bb)+(cc))
       e=[(from_id,query_data,str(datetime.now()),query_id)]
       cur.executemany('insert into users(id,sans,time,code) values(?,?,?,?)',e)
       cnn.commit()
       cnn.close()
       
    if query_data == 'سالمند':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='/الف', callback_data='الف'),InlineKeyboardButton(text='/ب', callback_data='ب')],
            [InlineKeyboardButton(text='/پ', callback_data='پ'),InlineKeyboardButton(text='/ت', callback_data='ت')],
            [InlineKeyboardButton(text='/ث', callback_data='ث'),InlineKeyboardButton(text='/ج', callback_data='ج')],
            [InlineKeyboardButton(text='/خروج', switch_inline_query='خروج')],
            ])
        bot.sendMessage(from_id, 'فيلم انيميشني مخصوص سالمندان  ', reply_markup=keyboard)


        if query_data== 'الف':
            bot.sendMessage(from_id, text=('مبارک باشه نوبت شما ثبت شد :\n')+(bb)+(cc))
            f=[(from_id,query_data,str(datetime.now()),query_id)
            cur.executemany('insert into users(id,sans,time,code) values(?,?,?,?)',f)
            cnn.commit()
            cnn.close()           

       
                       
TOKEN = sys.argv[0]

bot = telepot.Bot('ENTER API TOKEN')
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
