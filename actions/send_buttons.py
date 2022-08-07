from telegram import InlineKeyboardButton,InlineKeyboardMarkup,constants

# Telegram API Constants 
constants.MAX_POLL_OPTION_LENGTH=500

# Crate a buttons(INLINE BUTTONS ) array and then send it to the users dyanamically 
# We will get button name and the action associated with the button in this btnarr 
# We will create a keyboard array then and send it to the users
def send_button_dynamically(bot,chat_ids,btnarr):
    keyboard=[]
    if(len(btnarr)>=1):
        for btn in btnarr :
            btnname=btn['name']
            btnaction=btn['action']
            keyboard.append([InlineKeyboardButton(btnname, callback_data=btnaction)])
    else:
        print("Please Send Buttons Data...")
    reply_markup = InlineKeyboardMarkup(keyboard)
    for chat_id in chat_ids:
        bot.send_message(chat_id,text="Please select",reply_markup=reply_markup)


