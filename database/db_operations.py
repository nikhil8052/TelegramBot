
import mysql.connector
from constants import host,user,password

db=None 

# Open Local Database connection 
# def open():
#   global db 
#   db = mysql.connector.connect(
#   host='localhost',
#   user='root',
#   password='',
#   database='bot'
# )


# This open function for live Db 
def open():
  global db 
  db = mysql.connector.connect(
  host=host,
  user=user,
  password=password,
  database='bot'
)

# close database connection 
def close():
  global db 
  db.commit()
  db.close()


# For getting the data (SELECT COMMAND )
def select(query):
    open()
    mycursor = db.cursor()
    mycursor.execute(query)
    result = mycursor.fetchall()
    db.commit()
    close()
    return result


# For inserting the data in the database (INSERT COMMAND)
def insert(query,val):
    open()
    mycursor = db.cursor()
    mycursor.execute(query,val)
    db.commit()
    close()
    return 




