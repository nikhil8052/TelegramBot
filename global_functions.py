
# This function will give you the chat_id of user
def get_chat_id(update, context):
    chat_id = -1
    if update.message is not None:
        chat_id = update.message.chat.id
    elif update.callback_query is not None:
        chat_id = update.callback_query.message.chat.id
    elif update.poll is not None:
        chat_id = context.bot_data[update.poll.id]

    return chat_id


# Notigy single user via chat_id 
def notify_using_chat_id(chat_id,bot,text):
  bot.send_message(chat_id,text)
