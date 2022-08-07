import json
from telegram import Bot,InlineKeyboardButton,InlineKeyboardMarkup,Bot
import requests
from constants import api_key
from html_parser import html_parser
from global_functions import get_chat_id

# from html_parser import html_parser

# constants.PARSEMODE_HTML='HTML'
parser = html_parser.parser


# Global variables
all_quiz_questions = []
user_result=[]
question_count=1
correct_ans=0
wrong_ans=0
total_ques=0 

# Static Counter for keep track the question number to send to the boot


def static_counter():
    static_counter.counter += 1
    return static_counter.counter


static_counter.counter = -1


# To format the html text data into proper format using HTMLParser
def format_str(str):
    parser.feed(str)
    return parser.data


# Decode answers
def decode_ans(str):
    if str == 'A' or str=='opt1' :
        return 1
    elif str == 'B' or str=='opt2' :
        return 2
    elif str == 'C' or str=='opt3' :
        return 3
    elif str == 'D' or str=='opt4' :
        return 4

# Convert option to A,B,C,D 
def opt_to_ABCD(text):
  if text=='opt1':
    return 'A'
  elif text=='opt2':
    return 'B'
  elif text=='opt3':
    return 'C'
  elif text=='opt4':
    return 'D'

# To format the html text data into proper format using HTMLParser
# def format_str(str):
#     parser.feed(str)
#     return parser.data


# Get quiz questions from the database GraphQL
def get_questions_db():

    query = '''{
  getStudentExamQuestions(
    mobile: "9701908767"
    exam_session_id: 0
    type: "schedule_exam"
    exam_paper_id: 6641
  ) {
    id
    question
    option1
    option2
    option3
    option4
    bookmarked
    compquestion
    examType
    explanation
    qtype
    inputquestion
    list1type
    list2type
    mains_2021
    mat_question
    selection_type
    sub_exam_type
    subject
    subject_name
  }
}'''

    query1 = '''{
  getStudentExamQuestions(
    mobile: "9701908767"
    exam_session_id: 0
    type: "schedule_exam"
    exam_paper_id: 6641
  ) {
    id
    answer
  }
}'''
    global all_quiz_questions
    # url="http://rizee.in:4005/graphql"
    url = "http://35.231.1.23:4013/graphql"
    r = requests.post(url, json={'query': query})
    r1 = requests.post(url, json={'query': query1})
    data = json.loads(r.text)
    data1 = json.loads(r1.text)
    questions = data['data']['getStudentExamQuestions']
    i = 0
    for q in questions:
        # to form key value pair
        tem_arr = {}
        # To store all the options
        opts = []
        # Get the answer
        ans = data1['data']['getStudentExamQuestions'][i]
        i = i+1
        tem_arr['question'] = format_str(q['question'])
        opts.append(format_str(q['option1']))
        opts.append(format_str(q['option2']))
        opts.append(format_str(q['option3']))
        opts.append(format_str(q['option4']))
        tem_arr['options'] = opts
        tem_arr['correct_ans'] = decode_ans(ans['answer'])
        tem_arr['explanation'] = format_str(q['explanation'])
        tem_arr['id'] = q['id']
        all_quiz_questions.append(tem_arr)
    return all_quiz_questions


# Send the one question to the User  
def send_question(chat_id,question,question_id, options,q_count):
    bot = Bot(api_key)
    html_text = ''''''
    html_text = html_text+"<b>"+q_count+" . "+question+"</b>"+"\n"
    option_count = 1
    for o in options:
        html_text = html_text+str(option_count)+".  "+o+"\n"
        option_count = option_count+1
    bot.send_message(chat_id, html_text, parse_mode="HTML")
    data1=json.dumps({'type':'quiz-option','question-id':question_id,'text':'opt1'})
    data2=json.dumps({'type':'quiz-option','question-id':question_id,'text':'opt2'})
    data3=json.dumps({'type':'quiz-option','question-id':question_id,'text':'opt3'})
    data4=json.dumps({'type':'quiz-option','question-id':question_id,'text':'opt4'})
    keyboard = [
       [InlineKeyboardButton("Option A", callback_data=data1),InlineKeyboardButton("Option B", callback_data=data2),],
       [InlineKeyboardButton("Option C", callback_data=data3),InlineKeyboardButton("Option D", callback_data=data4)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id,"Please Select Your Answer", reply_markup=reply_markup) 


# Send all the Questions One by One 
def send_all_questions():
    if(static_counter.counter == 0):
        all_quiz_questions = get_questions_db()
        bot = Bot(api_key)
        html_text = ''''''
        q1 = '''<b>Let's Play Quiz Now 🎇🎇🎉</b>'''
        bot.send_message(5033354066, q1, parse_mode="HTML")

        question_count = 1
        op_count = 1
        for q in all_quiz_questions:
            ques = format_str(q['question'])+"\n"
            html_text = html_text+"<b>"+str(question_count)+" . "+ques+"</b>"
            options = q['options']
            for o in options:
                html_text = html_text+str(op_count)+".  "+o+"\n"
                op_count = op_count+1
            op_count = 1
            question_count = question_count+1
            html_text = html_text+"\n"

        bot.send_message(5033354066, html_text, parse_mode="HTML")


#  Send all the questions One By One  
def send_quiz(update,context):
  global all_quiz_questions
  global total_ques
  global correct_ans
  global wrong_ans
  chat_id=get_chat_id(update,context)
  bot_id=context.bot.id
  bot=context.bot
  if static_counter.counter == -1 :
    static_counter()
    all_quiz_questions = get_questions_db()
    total_ques=len(all_quiz_questions)
    ques=all_quiz_questions[static_counter.counter]['question']
    op=all_quiz_questions[static_counter.counter]['options']
    ques_id=all_quiz_questions[static_counter.counter]['id']
    send_question(chat_id,ques,ques_id,op,str(static_counter.counter+1))
  elif static_counter.counter < total_ques-1 :
    static_counter()
    ques=all_quiz_questions[static_counter.counter]['question']
    op=all_quiz_questions[static_counter.counter]['options']
    ques_id=all_quiz_questions[static_counter.counter]['id']
    send_question(chat_id,ques,ques_id,op,str(static_counter.counter+1))
  else:
    explanation=''' You have 🕢 successfully attemted the Quiz , It's time to check your result ⛑ \n\nNotice\n 1. ❌(Sign) indicates you attempted wrong answer.\n 2. ✅ (Sign) indicates you attempted correct answer.\n\n'''
    i=1
    for q in user_result:
      explanation=explanation+str(i)+". "+q['explanation']
      if q['correct_ans']==q['user_selected_ans']:
        correct_ans=correct_ans+1
        explanation=explanation+' ✅ \n\n'
      else:
        wrong_ans=wrong_ans+1
        explanation=explanation+' ❌ \n\n'

      i=i+1 
    sc="Your score is 🎈 " + "\n ✅  "+str(correct_ans)+"\n ❌  "+str(wrong_ans)
    bot.send_message(chat_id,text=explanation)
    bot.send_message(chat_id,text=sc)
    tem={"chat_id":chat_id,"questions":user_result,"bot_id":bot_id,"exam_paper_id":6641}
    print(tem)


#  When user will answer the Question then for sending the next question this function will be called based on the callback query 
def send_next(update,context):
  query = update.callback_query
  obj=json.loads(update.callback_query.data)
  sel_opt=obj['text']
  ques_id=obj['question-id']
  flag=False 
  # Check if user already answer the question in user result list
  for q in user_result:
    if q['id']==ques_id:
      flag=True  
      break 
# True if user already answer the question else send the next question
  if flag==True :
    text=''' You have already answered this question.'''
    context.bot.answer_callback_query(query.id,text=text)
    return 
  else:
    user_ans=opt_to_ABCD(sel_opt)
    cor_ans=all_quiz_questions[static_counter.counter]['correct_ans']
    if cor_ans == decode_ans(sel_opt):
      cor_text='You selected correct answer.'
      context.bot.answer_callback_query(query.id,text=cor_text)
    else:
      wrong_text='Opps , Your answer was wrong.'
      context.bot.answer_callback_query(query.id,text=wrong_text)
    
    # text=f'''You Selected {user_ans} '''
    print(static_counter.counter)
    all_quiz_questions[static_counter.counter]['user_selected_ans']=decode_ans(sel_opt)
    user_result.append(all_quiz_questions[static_counter.counter])
    send_quiz(update,context)
    
  


          
