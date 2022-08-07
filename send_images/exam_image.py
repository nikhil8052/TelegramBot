from telegram import Poll,InlineKeyboardButton,InlineKeyboardMarkup,constants
from bot import send_mobile_verification_button
import json 


# SHOW PLAY QUIZ BUTTON  
def show_quiz_button(bot,chat_id):
    data=json.dumps({'type':'playquiz'})
    keyboard = [
        [InlineKeyboardButton("Play Quiz ", callback_data=data)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text='''Play free 🎁Quiz with Rizee,enhance your 📚learning,let's do it together.Start 🔕Quiz now 🎈🎉🎊✨'''
    bot.send_message(chat_id,text=text,reply_markup=reply_markup)



# TO SEND THE IMAGE BASED ON THE EXAM USER SELECTED 
def send_image(update,context):
    bot=context.bot
    chat_id=update.callback_query.message.chat.id
    obj=json.loads(update.callback_query.data)
    
    caption='''Our 🖥productive Course for you people. Associate with Rizee for your bright future. Go through our courses and do it now ... 🤷‍♂️Don't wait for others if not now then never ..Hurry Up 🎉🎉🎉'''
    if obj['type']=='NEET':
        bot.send_photo(chat_id,"https://rizee.in/telegram/course_plans/NEET.jpeg",caption=caption)
        show_quiz_button(bot,chat_id)
    elif obj['type']=='JEE':
        bot.send_photo(chat_id,"https://rizee.in/telegram/course_plans/JEE.jpeg",caption=caption)
        show_quiz_button(bot,chat_id)
    elif obj['type']=='emcet_eng':
        bot.send_photo(chat_id,"https://rizee.in/telegram/course_plans/EAMCET_Eng.jpeg",caption=caption)
        show_quiz_button(bot,chat_id)
    elif obj['type']=='emcet_agr':
        bot.send_photo(chat_id,"https://rizee.in/telegram/course_plans/EAMCET_Agr.jpeg",caption=caption)
        show_quiz_button(bot,chat_id)


    
