
def send_messages_using_chatids(bot,ids,msg):
    for id in ids:
        print(" I am another fun ... ")
        print(id)
        bot.send_message(id,text=msg)