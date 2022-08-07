import requests
import json 
from telegram import InlineKeyboardButton,InlineKeyboardMarkup,Bot
from constants import api_key

def send_options():
   bot = Bot(api_key)
   keyboard = [
       [InlineKeyboardButton("Option A", callback_data='opt1'),InlineKeyboardButton("Option B", callback_data='opt2'),],
       [InlineKeyboardButton("Option C", callback_data='opt3'),InlineKeyboardButton("Option D", callback_data='opt4')],
    ]
   reply_markup = InlineKeyboardMarkup(keyboard)
   bot.send_message(5033354066,"Please Select Your Answer", reply_markup=reply_markup) 

