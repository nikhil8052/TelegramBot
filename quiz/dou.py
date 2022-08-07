from database import db_operations

def insert_result_into_db(quiz_result):
    bot_id=quiz_result['bot_id']
    chat_id=quiz_result['chat_id']
    exam_paper_id=quiz_result['exam_paper_id']
    questions=quiz_result['questions']
    attempted_answer=len(questions)
    for q in questions:
        user_sel=q['user_selected_option']
        correct_ans=q['correct_ans']
        id=q['id']
        status=get_status(user_sel,correct_ans)
        value=('',bot_id,chat_id,exam_paper_id,id,'',status,attempted_answer,correct_ans,1)
        q='insert into bot_quiz (id,bot_id,user_id,exam_paper_id,question_id,slno,status,attempted_answer,answer,estatus) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '
        db_operations.insert(q,value)

def get_status(user_sel,correct_ans):
    if user_sel==correct_ans:
        return '2'
    else:
        return '1'