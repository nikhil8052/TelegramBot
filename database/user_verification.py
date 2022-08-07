from database import db_operations


# Check whether user is new or already registered with us 
# Return false if user is new 
# If user is already registered with us send the details of the user 
def user_exist(chat_id):
    q=f'select * from user where chat_id={chat_id}'
    result=db_operations.select(q)
    print(len(result))
    print(result)
    if(len(result)>=1):
        return result
    else:
        return False 
    