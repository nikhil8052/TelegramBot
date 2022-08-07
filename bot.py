from glob import glob
from re import I
from telegram.ext import Updater,CallbackContext,PollAnswerHandler,CommandHandler,MessageHandler,Filters,CallbackQueryHandler,PollHandler
from telegram import InlineKeyboardButton,ReplyKeyboardRemove,InlineKeyboardMarkup,Update,Bot,Poll,ReplyKeyboardMarkup,KeyboardButton
from quiz import quiz, quiz1 
from database import user_verification,db_operations
from send_images import exam_image
from constants import api_key
import datetime 
import json 
from actions import send_buttons
from actions import send_messages
from quiz import quiz,quiz1
from buttons import exam_buttons
from flask import Flask,redirect, url_for, request
from global_functions import get_chat_id,notify_using_chat_id
from time import sleep
import command_handlers
# Telegram API Constants 

# Telegram API Constants 


app = Flask(__name__)


# global variables 
user_selected_exam=""
global_update=None
global_context=None 
global_bot=None


# This is the static counter 
def static_counter():
        static_counter.counter += 1
        return static_counter.counter
static_counter.counter = 0



# Updater is for continues update from the Telegram chatbot 
updater = Updater(token=api_key, use_context=True)
dispatcher = updater.dispatcher


# Whenever we will give the /start command to our boot this function will be excuted 
def start(update , context ):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


# Whenever user will send the first message then this function will be called 
def first_msg(update,context):
    global global_update
    global global_context 
    global global_bot
    global_context=context
    global_update=update
    global_bot=context.bot 
    chat_id=get_chat_id(update,context)
    bot=context.bot 
    name=update.message.chat.first_name
    
    result=user_verification.user_exist(chat_id)
    
    # FALSE MEANS USER IS NEW NEED TO REGISTER HIM/HER WITH US 
    if(result==False):
        q='''select * from action where action in ('welcome','Youtube Link') '''
        action_result=db_operations.select(q)
        welmsg=action_result[0][5]
        youtube_url=action_result[1][4]
        update.message.reply_text(welmsg)
        update.message.reply_text(youtube_url)
        # exam_buttons.send_exam_buttons(update,context)
        send_mobile_verification_button(chat_id)

        # if static_counter.countmer==0 :
        #     send_mobile_verification_button(update,context)
    else:
        name=result[0][1]
        chat_id=result[0][2]
        text=f'''Hi {name} , How can we help you ....?
        \n\nPlease click the following commands. 👇\n1. Play Quiz with Rizee 🧾💥 -- /Quiz\n2. See your score -- /myscore\n3. See our courses -- /courses\n4. Buy Course -- /buy\n5. Raise Doubt -- /doubt\n6. FAQ -- /faq\n7. Help me -- /helpme\n8. Build future strategies -- /build\n9. Avail offers -- /offer
        \nOur team ✌ is always with you 🤵.We provide support 📞 to you people for your bright 🎇 carrier Hurry Up and connect 🎁 with us.We are here for you ✨🎄🎈...
        '''
        update.message.reply_text(text)
    return ""

 
# WHEN THE USER WILL ALL THEIR PHONE NUMBER OR WHEN USER WILL CLICK ON ALLOW PHONE NUMBER BUTTON 
def contact_handler(update,context):
    chat_id=get_chat_id(update,context)
    name=update.message.chat.full_name
    phone_number=update.message.contact.phone_number
    bot=context.bot 
    
    is_registered=user_verification.user_exist(chat_id)
    bot.send_message(chat_id,' Hurry 🎉🎊 , Now you can use our services....Thanks for register yourself to Rizee.😊')
    static_counter()

    exam_buttons.send_exam_buttons(update,context)

    # quiz.show_quiz_button(bot,chat_id)
    # exam_image.send_image(update,context)

    # INSERT NEW USER DETAILS IN DATABASE 
    if is_registered==False :
        dt=datetime.datetime.now()
        values=('',name,chat_id,phone_number,1,dt)
        result=db_operations.insert('insert into user (id,name,chat_id,mobile,estatus,inserted_time) values(%s,%s,%s,%s,%s,%s)',values)
        bot.send_message(chat_id,' Hurry 🎉🎊 , Now you can use our services....Thanks for register yourself to Rizee.😊')
    else:
        bot.send_message(chat_id,'''You have already shared your 📱Mobile Number with Rizee , Now go ahead and explore Rizee 🏙 Services. Don't wait go now ''')

        



# To send the keyboard button to the user for getting the Phone Number  
def send_mobile_verification_button(chat_id):
    bot=Bot(api_key)
    markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Allow Phone Number',request_contact=True)]],one_time_keyboard=True)
    bot.send_message(chat_id,'Please Allow Your 📱Phone Number for further disscussion 🤷‍♂️🤷‍♂️ and Play free Quiz with us 🎉🎉🎉🎊', reply_markup=markup)



# All command handlers are here  
# Query handler when the button will be clicked 
def handle_callback_data(update, context):
    global user_selected_exam
    callback_query_response = update.callback_query.data
    chat_id=get_chat_id(update,context)
    bot=context.bot
    verify=" You are registerd successfully.Our agent will contact you soon"
    print(" This is the data from the callback query ")
    print(callback_query_response)
    print(" This is the object after converting it to the json to the dict ")
    obj=json.loads(callback_query_response)
    print(obj)
    
    if obj['type']=='playquiz':
        quiz.send_quiz(update,context)
    elif obj['type']=='NEET':
        user_selected_exam="NEET"
        notify_using_chat_id(chat_id,bot,verify)
    elif obj['type']=='JEE':
        user_selected_exam="JEE"
        notify_using_chat_id(chat_id,bot,verify)
    elif obj['type']=='emcet_eng':
        user_selected_exam="emcet_eng"
        notify_using_chat_id(chat_id,bot,verify)
    elif obj['type']=='emcet_agr':
        user_selected_exam="emcet_agr"
        notify_using_chat_id(chat_id,bot,verify)
    elif obj['type']=='quiz-option':
        quiz.send_next(update,context)

    # send_mobile_verification_button(update,context)



# Dispather is to to tell which function is called or associate to which command 
@app.route('/')
def fun():
    start_handler = CommandHandler('star', start)
    quiz_handler = CommandHandler('quiz', command_handlers.quiz_command_handler)
    myscore_handler = CommandHandler('myscore', command_handlers.myscore_command_handler)
    courses_handler = CommandHandler('courses', command_handlers.courses_command_handler)
    buy_handler = CommandHandler('buy', command_handlers.buy_command_handler)
    doubt_handler = CommandHandler('doubt', command_handlers.doubt_command_handler)
    faq_handler = CommandHandler('faq', command_handlers.faq_command_handler)
    helpme_handler = CommandHandler('helpme', command_handlers.helpme_command_handler)
    build_handler = CommandHandler('build', command_handlers.build_command_handler)
    offer_handler = CommandHandler('offer', command_handlers.offer_command_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(quiz_handler)
    dispatcher.add_handler(myscore_handler)
    dispatcher.add_handler(courses_handler)
    dispatcher.add_handler(buy_handler)
    dispatcher.add_handler(doubt_handler)
    dispatcher.add_handler(faq_handler)
    dispatcher.add_handler(helpme_handler)
    dispatcher.add_handler(build_handler)
    dispatcher.add_handler(offer_handler)
    dispatcher.add_handler(MessageHandler(Filters.text, first_msg))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(CallbackQueryHandler(handle_callback_data))
    # dispatcher.add_handler(PollHandler(quiz.poll_handler))
    updater.start_polling()
    return ""

@app.route('/sendbuttons',methods=['post','get'])
def fun1():
    bot=Bot(api_key)
    if request.method == 'POST':
      data = request.json
    global global_bot
    global global_update
    btns=json.loads(data)
    send_buttons.send_button_dynamically(bot,[5361834379,5033354066,1664876303,5129193582],btns['buttons'])
    return " done "

@app.route('/rambo',methods=['POST'])
def fun3():
    bot=Bot(api_key)
    if request.method =='POST':
        data=request.get_json(force=True) 
        # data=json.loads(data)
        print(data)
        send_messages.send_messages_using_chatids(bot,data['chat_ids'],data['message'])
    return "Kerta"


@app.route('/giveme',methods=['post','get'])
def fun4():
    result=db_operations.select('select * from user')
    data=[]
    for one in result :
        tem={}
        tem['name']=one[1]
        tem['chat_id']=one[2]
        tem['mobile_number']=one[3]
        tem['created_on']=one[4]
        data.append(tem)     
    return  json.dumps(data)
    # return result



if __name__ == '__main__':
    from waitress import serve
    serve(app,host='0.0.0.0',port=8080)
    print(" Bot has started ")
  


# if __name__ == '__main__':
#    app.run(debug=True,port=8080)

