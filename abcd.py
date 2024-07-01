import telebot
from pytube import YouTube
import scrapetube
import os
import datetime
bot = telebot.TeleBot('6348897063:AAExtb7SP-9mYr9xO1IEfN2vACFdknppeec')
msg = '''We will shutdown the server after 9pm everyday. Hence we can't serve your request which are sent after 9pm immediately. Anyways your request will automatically get served once the server gets active.
We are searching for better methods to Host the server. Soon we'll give 24/7 access.
Thank You for the support !! 
Musixquickbot Team 
(Automated response)'''
bot.send_message(6636725195,msg)
print("Done")