from global_functions import get_chat_id 
from quiz import quiz
      
def send_message(text,update,context):
    chat_id=get_chat_id(update,context)
    context.bot.send_message(chat_id,text)
    

# Quiz command handler 
def quiz_command_handler(update,context):
    quiz.static_counter.counter=-1
    quiz.correct_ans=0
    quiz.wrong_ans=0
    quiz.user_result=[]
    quiz.all_quiz_questions=[]
    quiz.send_quiz(update,context)

def myscore_command_handler(update,context):
    text="Opps!!, No score available."
    send_message(text,update,context)


def courses_command_handler(update,context) :
    text="We are sorry ?? Our team is working on this part to show you results this functionality will be availabe to you soon .... \n\n Enjoy learning with Rizee 🎇🎇🎇🎈🎈"
    send_message(text,update,context) 


def buy_command_handler(update,context) :
    text="We are sorry ?? Our team is working on this part to show you results this functionality will be availabe to you soon .... \n\n Enjoy learning with Rizee 🎇🎇🎇🎈🎈"
    send_message(text,update,context) 
 


def doubt_command_handler(update,context) :
    text="We are sorry ?? Our team is working on this part to show you results this functionality will be availabe to you soon .... \n\n Enjoy learning with Rizee 🎇🎇🎇🎈🎈"
    send_message(text,update,context) 



def faq_command_handler(update,context) :
    text="We are sorry ?? Our team is working on this part to show you results this functionality will be availabe to you soon .... \n\n Enjoy learning with Rizee 🎇🎇🎇🎈🎈"
    send_message(text,update,context) 



def helpme_command_handler(update,context) :
    text="We are sorry ?? Our team is working on this part to show you results this functionality will be availabe to you soon .... \n\n Enjoy learning with Rizee 🎇🎇🎇🎈🎈"
    send_message(text,update,context) 



def build_command_handler(update,context) :
    text="We are sorry ?? Our team is working on this part to show you results this functionality will be availabe to you soon .... \n\n Enjoy learning with Rizee 🎇🎇🎇🎈🎈"
    send_message(text,update,context) 



def offer_command_handler(update,context):
    text="We are sorry ?? Our team is working on this part to show you results this functionality will be availabe to you soon .... \n\n Enjoy learning with Rizee 🎇🎇🎇🎈🎈"
    send_message(text,update,context) 
 

