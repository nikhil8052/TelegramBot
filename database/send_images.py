from database import db_operations
import datetime


def get_exam_id(exam):
    if exam=='NEET':
        return '1'
    elif exam=='JEE':
        return '2'
    elif exam=='emcet_eng':
        return '3'
    elif exam=='emcet_agr':
        return '7'

    
def insert_exam(chat_id,exam):
    exam_id=get_exam_id(exam)
    dt=datetime.datetime.now()
    value=('',chat_id,2,exam_id,1,dt)
    q='insert into user_attribute (id,user_id,attribute_id,value,estatus,inserted_time) values(%s,%s,%s,%s,%s,%s)'
    db_operations.insert(q,value)


