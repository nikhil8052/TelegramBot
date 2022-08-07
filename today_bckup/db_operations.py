import mysql.connector
from constants import host,user,password
# db = mysql.connector.connect(
#   host='localhost',
#   user='root',
#   password='',
#   database='bot'
# )

# db = mysql.connector.connect(
#   host='34.74.241.2',
#   user='rspace',
#   password='Rsp@2019',
#   database='bot'
# )

def getConnection():
  try:
    db = mysql.connector.connect( host='34.74.241.2',port=3306,
  user='rspace',
  password='Rsp@2019',
  database='bot')
  except mysql.connector.Error as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
     else:
        db.close()
  return mydb

# For getting the data (SELECT COMMAND )
def select(query):
    mycursor1 = getConnection()
    mycursor = mycursor1.cursor()
    mycursor.execute(query)
    result = mycursor.fetchall()
    db.commit()
    return result


# For inserting the data in the database (INSERT COMMAND)
def insert(query,val):
    mycursor = db.cursor()
    mycursor.execute(query,val)
    db.commit()
    return ""


