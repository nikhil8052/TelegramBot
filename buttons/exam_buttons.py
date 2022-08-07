from telegram import InlineKeyboardButton,InlineKeyboardMarkup,constants
import json 
from database import db_operations

# TO SEND THE EXAM SELECTION BUTTONS TO THE USERS 
def send_exam_buttons(update,context):
    neet=json.dumps({'type':'NEET'})
    jee=json.dumps({'type':'JEE'})
    emcet_eng=json.dumps({'type':'emcet_eng'})
    emcet_agr=json.dumps({'type':'emcet_agr'})
    keyboard = [
       [InlineKeyboardButton("NEET", callback_data=neet)],
       [InlineKeyboardButton("JEE", callback_data=jee)],
       [InlineKeyboardButton("EAMCET – ENGINNERING", callback_data=emcet_eng)],
       [InlineKeyboardButton("EAMCET – AGRICULTURE", callback_data=emcet_agr)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Please Select Your Course to play Quiz", reply_markup=reply_markup) 



